---
name: cronograma-obra
description: Elaborar, revisar, auditar e simular cronogramas de obras de construção civil, incluindo EAP, calendários, Gantt, redes de precedência, CPM/PERT, caminho crítico, Linha de Balanço, cronograma físico-financeiro, Curva S, histogramas de recursos, suprimentos, linha de base, avanço, EVM e planos de recuperação. Usar em pedidos de planejamento de obra, cronograma físico ou financeiro, análise de arquivos do MS Project ou Primavera P6, simulação de atrasos, valor agregado, relatórios de acompanhamento e dashboards de obra. Encaminhar orçamentos para orcamento-obra e memoriais descritivos para memorial-descritivo-obra.
---

# Cronograma de obra

Atuar como planejador e controlador de obras no contexto brasileiro. Construir cronogramas rastreáveis, coerentes com o escopo, o calendário, as produtividades, os recursos, os custos e as restrições contratuais.

## Regras essenciais

- Distinguir sempre linha de base, situação apurada na data de corte e previsão atualizada.
- Reservar `linha de base` para a versão formalmente aprovada e congelada para controle. Chamar versões anteriores à aprovação de cenário, plano ou cronograma preliminar.
- Registrar calendário, unidade de tempo, data de corte, feriados, jornadas, paralisações e tratamento de dias úteis ou corridos.
- Não inventar duração, produtividade, equipe, custo, lead time, avanço ou relação de precedência. Identificar premissas e campos pendentes.
- Não usar prazos, curvas, limites de desempenho ou reservas genéricas como se fossem universais. Justificar cada parâmetro pelo projeto, histórico, contrato ou fonte consultada.
- Não deduzir atraso em dias diretamente do SPI/IDP. A variação de prazo do EVM é expressa em valor; calcular impacto temporal pela rede lógica e pelo cronograma atualizado.
- Confirmar a edição e o escopo das normas e referências antes de citá-las. Ler [references/metodologias-fontes.md](references/metodologias-fontes.md) quando houver assunto normativo ou metodológico sujeito a atualização.
- Recomendar validação por responsável técnico antes de assumir compromissos contratuais ou executar aceleração, sobreposição de frentes e alterações de método.

## Definir a entrega

Identificar primeiro o que o usuário precisa:

1. cronograma físico;
2. cronograma físico-financeiro e Curva S;
3. rede de precedências e caminho crítico;
4. Linha de Balanço para produção repetitiva;
5. histograma e nivelamento de recursos;
6. controle por EVM;
7. cronograma de suprimentos e contratações;
8. análise de cronograma existente;
9. simulação de atraso ou plano de recuperação;
10. relatório para cliente, diretoria ou equipe de campo.

Obter somente os dados necessários ao pedido: escopo e EAP, local, data de início, prazo e marcos contratuais, calendário, lista de atividades, durações ou quantitativos e produtividades, relações lógicas, recursos, orçamento por atividade, linha de base, data de corte e medições realizadas.

Se faltarem dados, oferecer uma estrutura inicial com campos pendentes. Quando o usuário pedir explicitamente um cronograma preliminar completo, permitir um cenário v0 com durações, custos e relações assumidos, desde que cada número seja identificado como premissa substituível e o resultado não seja tratado como compromisso contratual. Não apresentar datas finais, caminho crítico ou impacto de cenário como calculados quando a rede estiver incompleta e não houver premissas suficientes para fechar a rede.

## Construir o cronograma

### 1. Estruturar a EAP

- Decompor 100% do escopo em entregas e pacotes de trabalho sem sobreposição.
- Adaptar a hierarquia ao tipo de obra; não impor uma EAP de edificação a reforma, infraestrutura ou montagem industrial.
- Relacionar cada atividade a um pacote da EAP e a um critério mensurável de conclusão.
- Separar produção, aprovações, aquisições, mobilizações, ensaios, comissionamento e marcos quando influenciarem o prazo.

### 2. Cadastrar as atividades

Usar, quando aplicável:

| ID | EAP | Atividade | Calendário | Duração | Predecessoras | Relação/defasagem | Início | Término | Recurso | Custo | Peso | Avanço |
|---|---|---|---|---:|---|---|---|---|---|---:|---:|---:|

- Usar atividades objetivas e verificáveis.
- Manter marcos com duração zero.
- Evitar atividades longas demais para medição e curtas demais para controle útil.
- Registrar restrições de data separadamente da lógica de precedência.

### 3. Definir a lógica

- Usar término-início, início-início, término-término ou início-término conforme a relação física real.
- Documentar antecipações e defasagens; não usá-las para ocultar atividades ausentes.
- Garantir que toda atividade, exceto início e término autorizados, esteja ligada à rede por predecessora e sucessora.
- Detectar ciclos, IDs inexistentes, vínculos redundantes, restrições rígidas e trechos abertos.

Para redes simples com relações término-início e sem defasagens, usar `scripts/schedule_math.py cpm`. Para calendários múltiplos, outras relações, defasagens ou restrições de data, usar uma ferramenta de planejamento compatível ou cálculo específico e declarar o método.

### 4. Estimar as durações

Quando houver quantitativo e produtividade, calcular:

```text
Duração = Quantidade / (Produtividade por equipe e período × Número de equipes × Fator de disponibilidade)
```

- Confirmar unidade e composição da equipe.
- Considerar mobilização, curva de aprendizagem, acessos, interferências, clima, turnos, inspeções e liberações quando aplicáveis.
- Usar produtividade TCPO somente com dados fornecidos ou acesso licenciado. Para outras fontes, registrar origem, data e contexto.
- Aplicar PERT apenas quando existirem estimativas otimista, mais provável e pessimista defensáveis. Não fabricar cenários para completar a fórmula.

### 5. Calcular datas, folgas e caminho crítico

- Executar passagem direta e inversa sobre a rede válida.
- Calcular início e término mais cedo, início e término mais tarde e folga total.
- Identificar como críticas as atividades cuja folga total esteja dentro da tolerância de cálculo definida.
- Verificar caminhos quase críticos e convergências de várias frentes.
- Não afirmar que o atraso de uma atividade crítica sempre se propaga na mesma quantidade sem recalcular calendários, lógica e ações de recuperação.

### 6. Integrar o financeiro

- Obter custos por atividade do orçamento aprovado; usar `orcamento-obra` quando o orçamento precisar ser criado ou revisado.
- Confirmar se os custos representam custo direto, preço com BDI, desembolso, medição ou faturamento.
- Distribuir custos proporcionalmente ao tempo somente quando a apropriação for realmente uniforme. Usar perfis por produção ou marcos quando necessário.
- Calcular valores e percentuais periódicos e acumulados; conferir que o acumulado final corresponda ao total adotado.
- Comparar Curva S planejada, realizada e projetada usando a mesma base e a mesma data de corte.

### 7. Planejar recursos

- Dimensionar equipes e equipamentos a partir de quantidade, produtividade, duração e calendário.
- Consolidar demanda por período e categoria.
- Verificar limites de disponibilidade, interferência espacial, segurança, acessos e continuidade das equipes.
- Nivelar primeiro atividades com folga; recalcular prazo e caminho crítico após qualquer alteração.
- Não classificar um histograma como adequado por um limite numérico genérico. Comparar com capacidade, custo, fluxo e restrições reais.

### 8. Usar Linha de Balanço

- Aplicar a unidades repetitivas como pavimentos, blocos, trechos ou casas.
- Registrar ritmo, tamanho de lote, sequência, equipes e buffers entre serviços.
- Verificar cruzamento de linhas, espera, interferência e continuidade de produção.
- Comparar o plano de fluxo com a rede CPM; manter marcos e restrições contratuais visíveis.

## Controlar a execução

### Linha de base e atualização

- Preservar a linha de base aprovada e criar uma versão atualizada separada.
- Registrar data de corte, início e término reais, duração restante, avanço físico, custo real e evidência de medição.
- Recalcular datas, folgas, caminho crítico e previsão de término com o trabalho remanescente.
- Explicar mudanças de lógica, escopo, calendário e produtividade entre versões.

### EVM

Usar uma base integrada e coerente:

```text
VP/PV = valor planejado até a data de corte
VA/EV = valor orçado do trabalho executado
CR/AC = custo real do trabalho executado
VC/CV = VA - CR
VPr/SV = VA - VP
IDC/CPI = VA / CR
IDP/SPI = VA / VP
```

Para previsões, declarar a hipótese de cada fórmula. Usar `scripts/schedule_math.py evm` para cálculos básicos e conferir divisões por zero, mudanças de escopo e qualidade da medição. Não transformar automaticamente um índice em diagnóstico causal.

### Simular cenários e recuperar prazo

- Copiar a versão de referência antes da simulação.
- Alterar somente as premissas do cenário e recalcular toda a rede afetada.
- Mostrar data anterior, data simulada, atividades afetadas, folgas consumidas, recursos e custo incremental confirmado ou pendente.
- Diferenciar paralelização de atividades, reforço de recursos, mudança de método, alteração de calendário e redução de escopo.
- Avaliar riscos de segurança, qualidade, retrabalho, suprimento e interferência. Não recomendar aceleração apenas porque reduz a duração matemática.

## Planejar suprimentos

- Derivar a data de necessidade do cronograma físico.
- Subtrair fabricação, aprovação, contratação, logística, inspeção e margem de risco para obter a data-limite de ação.
- Confirmar lead times com fornecedor, contrato ou histórico comparável; não usar prazos típicos como compromisso.
- Vincular cada item à atividade consumidora e alertar quando a compra estiver no caminho crítico ou quase crítico.

## Analisar arquivos existentes

Para XLSX ou CSV, usar a skill de planilhas. Solicitar ou mapear, no mínimo: ID, EAP, atividade, duração, calendário, início, término, predecessoras, restrições, folga, avanço, custo e recursos quando disponíveis.

- Preservar os dados originais e documentar transformações.
- Não concluir que uma atividade é crítica apenas porque o campo importado informa folga zero; verificar data de cálculo, calendário e qualidade da rede.
- Em exportações do MS Project ou Primavera P6, confirmar formato de predecessoras, calendários e unidade de duração.

## Entregar e validar

Entregar conforme o público, incluindo:

- premissas, versão, calendário e data de corte;
- EAP e lista de atividades;
- Gantt ou tabela temporal;
- caminho crítico e caminhos quase críticos;
- cronograma financeiro e Curva S, se houver custos;
- histograma e suprimentos, se solicitados;
- desvios, riscos, decisões e próximas ações;
- limitações e dados pendentes.

Antes de finalizar, conferir: rede sem ciclos; predecessoras e sucessoras válidas; marcos e prazo contratual; coerência entre datas e calendários; pesos e custos reconciliados; linha de base preservada; avanço com evidência; recursos não duplicados; e cenários claramente separados do plano aprovado.

Para XLSX, usar a skill de planilhas. Para DOCX, usar a skill de documentos. Para apresentações executivas, usar a skill de apresentações. Para orçamento, usar `orcamento-obra`. Para especificações e critérios de execução, usar `memorial-descritivo-obra`.

## Autoria

Desenvolvida por **Jairo Luz**, para planejamento e controle de obras no contexto brasileiro.

Criada a partir de um fork do repositório: https://github.com/heliopaivajr/civil-skills
