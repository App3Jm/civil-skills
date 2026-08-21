#!/usr/bin/env python3
"""Cálculos determinísticos de CPM simples e EVM.

O CPM aceita apenas relações término-início, sem defasagens e com um único
calendário. Use uma ferramenta de planejamento para redes mais complexas.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from collections import deque
from pathlib import Path


def finite_nonnegative(value: str) -> float:
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise argparse.ArgumentTypeError("o valor deve ser finito e não negativo")
    return number


def split_predecessors(value: str) -> list[str]:
    return [item for item in re.split(r"[;,\s]+", value.strip()) if item]


def read_activities(path: Path) -> tuple[list[str], dict[str, dict[str, object]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"id", "duration", "predecessors"}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"colunas obrigatórias ausentes: {', '.join(sorted(missing))}")

        order: list[str] = []
        activities: dict[str, dict[str, object]] = {}
        for line_number, row in enumerate(reader, start=2):
            activity_id = (row.get("id") or "").strip()
            if not activity_id:
                raise ValueError(f"linha {line_number}: id vazio")
            if activity_id in activities:
                raise ValueError(f"linha {line_number}: id duplicado {activity_id!r}")

            try:
                duration = float((row.get("duration") or "").strip())
            except ValueError as exc:
                raise ValueError(f"linha {line_number}: duração inválida") from exc
            if not math.isfinite(duration) or duration < 0:
                raise ValueError(f"linha {line_number}: duração deve ser finita e não negativa")

            predecessors = split_predecessors(row.get("predecessors") or "")
            activities[activity_id] = {
                "id": activity_id,
                "name": (row.get("name") or activity_id).strip(),
                "duration": duration,
                "predecessors": predecessors,
                "successors": [],
            }
            order.append(activity_id)

    if not order:
        raise ValueError("o arquivo não contém atividades")

    for activity_id in order:
        predecessors = activities[activity_id]["predecessors"]
        assert isinstance(predecessors, list)
        for predecessor in predecessors:
            if predecessor not in activities:
                raise ValueError(
                    f"atividade {activity_id!r}: predecessora inexistente {predecessor!r}"
                )
            if predecessor == activity_id:
                raise ValueError(f"atividade {activity_id!r}: autorreferência")
            successors = activities[predecessor]["successors"]
            assert isinstance(successors, list)
            successors.append(activity_id)

    return order, activities


def topological_order(
    order: list[str], activities: dict[str, dict[str, object]]
) -> list[str]:
    position = {activity_id: index for index, activity_id in enumerate(order)}
    indegree = {
        activity_id: len(activities[activity_id]["predecessors"]) for activity_id in order
    }
    queue = deque(activity_id for activity_id in order if indegree[activity_id] == 0)
    result: list[str] = []

    while queue:
        activity_id = queue.popleft()
        result.append(activity_id)
        successors = activities[activity_id]["successors"]
        assert isinstance(successors, list)
        for successor in sorted(successors, key=position.get):
            indegree[successor] -= 1
            if indegree[successor] == 0:
                queue.append(successor)

    if len(result) != len(order):
        cyclic = [activity_id for activity_id in order if indegree[activity_id] > 0]
        raise ValueError(f"a rede contém ciclo envolvendo: {', '.join(cyclic)}")
    return result


def calculate_cpm(path: Path, tolerance: float) -> dict[str, object]:
    order, activities = read_activities(path)
    sequence = topological_order(order, activities)

    early_start: dict[str, float] = {}
    early_finish: dict[str, float] = {}
    for activity_id in sequence:
        predecessors = activities[activity_id]["predecessors"]
        assert isinstance(predecessors, list)
        early_start[activity_id] = max(
            (early_finish[predecessor] for predecessor in predecessors), default=0.0
        )
        duration = activities[activity_id]["duration"]
        assert isinstance(duration, float)
        early_finish[activity_id] = early_start[activity_id] + duration

    project_duration = max(early_finish.values())
    late_start: dict[str, float] = {}
    late_finish: dict[str, float] = {}
    for activity_id in reversed(sequence):
        successors = activities[activity_id]["successors"]
        assert isinstance(successors, list)
        late_finish[activity_id] = min(
            (late_start[successor] for successor in successors), default=project_duration
        )
        duration = activities[activity_id]["duration"]
        assert isinstance(duration, float)
        late_start[activity_id] = late_finish[activity_id] - duration

    rows: list[dict[str, object]] = []
    for activity_id in order:
        total_float = late_start[activity_id] - early_start[activity_id]
        rows.append(
            {
                "id": activity_id,
                "name": activities[activity_id]["name"],
                "duration": activities[activity_id]["duration"],
                "predecessors": activities[activity_id]["predecessors"],
                "early_start": early_start[activity_id],
                "early_finish": early_finish[activity_id],
                "late_start": late_start[activity_id],
                "late_finish": late_finish[activity_id],
                "total_float": total_float,
                "critical": abs(total_float) <= tolerance,
            }
        )

    return {
        "method": "CPM término-início, sem defasagens, calendário único",
        "project_duration": project_duration,
        "tolerance": tolerance,
        "activities": rows,
    }


def safe_divide(numerator: float, denominator: float) -> float | None:
    return numerator / denominator if denominator != 0 else None


def calculate_evm(bac: float, pv: float, ev: float, ac: float) -> dict[str, object]:
    cpi = safe_divide(ev, ac)
    spi = safe_divide(ev, pv)
    eac_cpi = safe_divide(bac, cpi) if cpi not in (None, 0) else None
    return {
        "inputs": {"BAC": bac, "PV": pv, "EV": ev, "AC": ac},
        "CV": ev - ac,
        "SV": ev - pv,
        "CPI": cpi,
        "SPI": spi,
        "EAC_if_cost_efficiency_persists": eac_cpi,
        "ETC_if_cost_efficiency_persists": None if eac_cpi is None else eac_cpi - ac,
        "VAC_if_cost_efficiency_persists": None if eac_cpi is None else bac - eac_cpi,
        "TCPI_to_BAC": safe_divide(bac - ev, bac - ac),
        "warning": "SV é expresso em valor; não representa atraso em unidades de tempo.",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    cpm = subparsers.add_parser("cpm", help="calcular CPM simples a partir de CSV")
    cpm.add_argument("--input", required=True, type=Path, help="CSV UTF-8")
    cpm.add_argument("--tolerance", type=finite_nonnegative, default=1e-9)

    evm = subparsers.add_parser("evm", help="calcular indicadores básicos de EVM")
    evm.add_argument("--bac", required=True, type=finite_nonnegative)
    evm.add_argument("--pv", required=True, type=finite_nonnegative)
    evm.add_argument("--ev", required=True, type=finite_nonnegative)
    evm.add_argument("--ac", required=True, type=finite_nonnegative)

    parser.add_argument("--compact", action="store_true", help="emitir JSON compacto")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "cpm":
            result = calculate_cpm(args.input, args.tolerance)
        else:
            result = calculate_evm(args.bac, args.pv, args.ev, args.ac)
    except (OSError, ValueError) as exc:
        print(f"erro: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(result, ensure_ascii=False, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
