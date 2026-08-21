# Civil Skills para Construção Civil

> Skills especializadas em orçamento, planejamento e documentação técnica de obras no Brasil, adaptadas para uso no ChatGPT e no Codex.

[![Skills](https://img.shields.io/badge/skills-3-blue.svg)](#skills-disponíveis)
[![Idioma](https://img.shields.io/badge/idioma-pt--BR-green.svg)](#visão-geral)
[![Licença](https://img.shields.io/badge/licença-MIT-yellow.svg)](#autoria-licença-e-origem)

## Sumário

- [Visão geral](#visão-geral)
- [Skills disponíveis](#skills-disponíveis)
- [Como as skills trabalham juntas](#como-as-skills-trabalham-juntas)
- [Instalação](#instalação)
- [Como usar](#como-usar)
- [Orçamento de obra](#orçamento-de-obra)
- [Cronograma de obra](#cronograma-de-obra)
- [Memorial descritivo de obra](#memorial-descritivo-de-obra)
- [Arquivos e formatos de entrega](#arquivos-e-formatos-de-entrega)
- [Critérios técnicos e limitações](#critérios-técnicos-e-limitações)
- [Estrutura do pacote](#estrutura-do-pacote)
- [Autoria, licença e origem](#autoria-licença-e-origem)

## Visão geral

Este pacote reúne três skills voltadas à construção civil brasileira:

- `orcamento-obra`, para custos, quantitativos, composições, BDI e auditoria orçamentária;
- `cronograma-obra`, para planejamento, controle, simulações e cronograma físico-financeiro;
- `memorial-descritivo-obra`, para especificações técnicas, diagnóstico documental e critérios de execução e aceitação.

As skills foram revisadas para trabalhar com informações rastreáveis, separar dados confirmados de premissas e evitar o preenchimento de lacunas técnicas com valores inventados. Elas podem analisar arquivos fornecidos pelo usuário e gerar entregas em texto estruturado, XLSX, DOCX, PDF ou apresentações, conforme a necessidade e as ferramentas disponíveis.

O alvo principal desta edição é o sistema de Skills do ChatGPT e do Codex. A estrutura `SKILL.md` pode ser aproveitada por outros agentes compatíveis, mas caminhos, metadados, comandos e ferramentas podem exigir adaptação.

## Skills disponíveis

| Skill | Função principal | Recursos |
|---|---|---|
| [`orcamento-obra`](./skills/orcamento-obra/SKILL.md) | Elaborar, revisar e auditar orçamentos | Estimativa paramétrica, quantitativos, composições próprias, SINAPI, SICRO, TCPO autorizado, mercado, BIM, encargos, administração local, BDI e Curva ABC |
| [`cronograma-obra`](./skills/cronograma-obra/SKILL.md) | Elaborar, revisar, auditar e simular cronogramas | EAP, calendários, Gantt, CPM/PERT, caminho crítico, Linha de Balanço, Curva S, recursos, suprimentos, EVM e recuperação de prazo |
| [`memorial-descritivo-obra`](./skills/memorial-descritivo-obra/SKILL.md) | Elaborar e diagnosticar memoriais e especificações | Inventário documental, classificação de definições e pendências, especificações por disciplina, tabelas de acabamentos, critérios de aceitação e documentação *as built* |

## Como as skills trabalham juntas

Cada skill mantém um limite claro de responsabilidade:

| Necessidade principal | Skill responsável | Encaminhamento complementar |
|---|---|---|
| Quantificar e calcular custos | `orcamento-obra` | Consulta o memorial para definir o serviço e o cronograma para distribuir custos no tempo |
| Planejar prazos e sequência | `cronograma-obra` | Usa os custos do orçamento e os métodos, restrições e critérios definidos no memorial |
| Especificar materiais e execução | `memorial-descritivo-obra` | Encaminha cálculos de custos ao orçamento e planejamento temporal ao cronograma |

Em uma análise integrada, o fluxo recomendado é iterativo:

1. diagnosticar projetos, escopo, especificações, conflitos e pendências;
2. consolidar quantitativos, fontes de preços, custos diretos, administração local e BDI;
3. estruturar EAP, atividades, precedências, recursos, custos por período e linha de base;
4. reconciliar alterações entre memorial, orçamento e cronograma antes da entrega.

## Instalação

Para instalar no ChatGPT ou no Codex, importar cada pasta completa da skill. Não enviar somente o `SKILL.md` quando a pasta também contiver referências, scripts, metadados ou recursos.

Para baixar as três skills de uma vez, usar o arquivo [`files.zip`](./files.zip) disponível na raiz deste repositório.

Estrutura mínima esperada:

```text
nome-da-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
├── scripts/
└── assets/
```

Nem todas as skills usam todas essas pastas. Deve-se preservar apenas os arquivos existentes no pacote.

Ao transferir para outra ferramenta compatível com `SKILL.md`, consultar a documentação dessa ferramenta para definir o diretório de instalação e a sintaxe de chamada. Os metadados de `agents/openai.yaml` foram preparados para a interface do ChatGPT/Codex e podem ser ignorados por outros agentes.

## Como usar

A skill pode ser selecionada no painel de Skills ou citada pelo nome na solicitação. Dependendo da interface, a chamada pode aparecer como `@nome-da-skill` ou `$nome-da-skill`. Também é possível descrever a tarefa em linguagem natural para que a skill adequada seja selecionada pelo contexto.

Para respostas mais confiáveis, fornecer:

- objetivo da análise e formato de entrega;
- identificação, tipo e localização da obra;
- fase do empreendimento;
- projetos, memoriais, planilhas e revisões disponíveis;
- data-base, calendário, marcos ou exigências contratuais aplicáveis;
- escopo incluído, excluído e decisões já aprovadas.

Quando faltarem dados, as skills podem criar estruturas preliminares com premissas e campos pendentes. Esses resultados não devem ser tratados automaticamente como orçamento final, linha de base contratual, documento apto para licitação ou registro *as built*.

## Orçamento de obra

Usar `orcamento-obra` para:

- estimativas paramétricas e custo por metro quadrado;
- levantamento e conferência de quantitativos;
- planilhas analíticas e composições de custos unitários;
- bases SINAPI, SICRO, TCPO fornecido ou licenciado, CUB, mercado e composições próprias;
- orçamento BIM com rastreabilidade dos elementos e quantitativos;
- encargos sociais, administração local, mobilização, canteiro e BDI;
- Curva ABC, auditoria de planilhas e comparação de propostas;
- entregas em XLSX, DOCX ou texto estruturado.

Informações recomendadas:

- finalidade do orçamento;
- tipo da obra e natureza pública ou privada;
- cidade e UF;
- base e competência de preços;
- regime desonerado ou não desonerado;
- projetos, quantitativos e especificações disponíveis;
- área, padrão construtivo, escopo e exclusões.

Exemplos de solicitação:

```text
Use @orcamento-obra para elaborar um orçamento analítico de uma escola municipal
em Recife/PE. Utilize SINAPI, informe a competência consultada, separe custos
diretos, administração local e BDI e entregue uma planilha XLSX auditável.

Use @orcamento-obra para revisar a planilha anexada. Confira quantitativos,
unidades, fontes, competência, duplicidades, BDI e Curva ABC. Liste as divergências
antes de propor qualquer correção.

Use @orcamento-obra para criar uma estimativa preliminar desta reforma. Onde não
houver dado suficiente, registre a premissa ou deixe o campo pendente.
```

## Cronograma de obra

Usar `cronograma-obra` para:

- EAP e lista de atividades;
- calendários, relações de precedência e gráfico de Gantt;
- CPM/PERT, folgas, caminho crítico e caminhos quase críticos;
- Linha de Balanço para blocos, pavimentos, trechos ou unidades repetitivas;
- cronograma físico-financeiro e Curva S;
- histogramas, nivelamento de recursos e cronograma de suprimentos;
- linha de base, atualização de avanço e previsão de término;
- EVM com VP, VA, CR, IDC, IDP e projeções justificadas;
- simulações de atraso e planos de recuperação;
- análise de exportações do MS Project e do Primavera P6.

Informações recomendadas:

- escopo, EAP ou lista de atividades;
- data de início, prazo, marcos e calendário;
- durações ou quantitativos e produtividades;
- predecessoras, defasagens e restrições;
- equipes, equipamentos e limites de disponibilidade;
- custos por atividade;
- linha de base, data de corte e medições realizadas.

Exemplos de solicitação:

```text
Use @cronograma-obra para elaborar um cronograma físico-financeiro preliminar.
Monte a EAP, registre as premissas de duração, crie a rede lógica, identifique o
caminho crítico e gere a Curva S. Não trate o cenário como linha de base aprovada.

Use @cronograma-obra para analisar o XLS exportado do MS Project. Verifique a
qualidade da rede, atividades sem sucessoras, restrições rígidas, folgas, caminho
crítico e coerência do avanço na data de corte informada.

Use @cronograma-obra para simular um atraso de três semanas na estrutura. Preserve
a linha de base, recalcule a rede e apresente impacto no término, atividades
afetadas, riscos e alternativas de recuperação.
```

O arquivo `scripts/schedule_math.py` apoia cálculos determinísticos de CPM para redes simples e indicadores básicos de EVM. Redes com calendários múltiplos, defasagens, restrições ou relações diferentes de término-início exigem ferramenta ou cálculo compatível com essa complexidade.

## Memorial descritivo de obra

Usar `memorial-descritivo-obra` para:

- memoriais de obra nova, reforma, retrofit, ampliação e interiores;
- cadernos de especificações e tabelas de acabamentos;
- arquitetura, estrutura, fundações e impermeabilização;
- instalações hidrossanitárias, elétricas, dados, SPDA e climatização;
- incêndio, acessibilidade, áreas externas e resíduos;
- memoriais para orçamento, compras, execução, licitação e entrega;
- diagnóstico de projetos, conflitos e omissões;
- documentação *as built* baseada em registros verificados.

Cada requisito é classificado como:

- `DEFINIDO`: há fonte suficiente e coerente;
- `PARCIAL`: existem dados, mas faltam parâmetros necessários;
- `PENDENTE`: não há fonte ou decisão;
- `CONFLITANTE`: documentos ou decisões divergem;
- `NÃO APLICÁVEL`: item analisado e excluído com justificativa.

Informações recomendadas:

- tipo, uso e fase do memorial;
- disciplinas contempladas e excluídas;
- localização, ocupação e uso da edificação;
- projetos, revisões, levantamentos e aprovações;
- finalidade: contratação, orçamento, execução, operação ou entrega;
- nível de detalhamento e formato final.

Exemplos de solicitação:

```text
Use @memorial-descritivo-obra para diagnosticar os projetos anexos. Classifique
as informações como DEFINIDO, PARCIAL, PENDENTE ou CONFLITANTE e indique o impacto
de cada lacuna no orçamento, no prazo e na execução.

Use @memorial-descritivo-obra para redigir um memorial técnico por disciplina,
com critérios verificáveis de execução, inspeção, ensaio e aceitação. Não invente
marcas, dimensões ou capacidades que não estejam nos documentos.

Use @memorial-descritivo-obra para preparar uma minuta para futura licitação.
Como os projetos ainda estão incompletos, separe requisitos de desempenho e
pendências impeditivas e não classifique o documento como apto para licitar.
```

## Arquivos e formatos de entrega

| Formato | Uso recomendado |
|---|---|
| Markdown ou texto estruturado | Diagnósticos, premissas, tabelas simples e conteúdo para revisão |
| XLSX | Orçamento, quantitativos, cronograma físico-financeiro, Curva S, EVM e controles tabulares |
| DOCX | Memorial descritivo, relatório técnico, auditoria e relatório de acompanhamento |
| PDF | Versão controlada para distribuição, após revisão visual |
| PPTX | Apresentação executiva de prazo, custos, riscos e decisões |
| CSV/XLSX exportado | Entrada para análise de MS Project, Primavera P6 ou outros sistemas |

As planilhas devem manter fórmulas auditáveis. Documentos e PDFs devem ser revisados quanto a paginação, tabelas, títulos e legibilidade antes da entrega.

## Critérios técnicos e limitações

As três skills seguem estes princípios:

- informar fonte, localidade, competência e data-base quando aplicável;
- distinguir documento confirmado, cálculo, hipótese, estimativa e pendência;
- não inventar códigos, preços, quantitativos, durações, normas ou especificações;
- verificar normas, legislação, tributos e bases de preços quando puderem ter mudado;
- não reproduzir conteúdo protegido de bases como TCPO sem acesso autorizado;
- preservar linha de base e dados originais ao analisar arquivos existentes;
- registrar conflitos e solicitar decisão formal quando a ordem de precedência não estiver definida;
- recomendar revisão e responsabilidade técnica por profissional habilitado antes de licitar, contratar ou executar.

Aplicações específicas:

- segurança de obra deve considerar a NR-18 vigente e o PGR aplicável; PCMAT não é adotado como exigência atual genérica;
- incêndio deve considerar ocupação, área, altura, risco e regras do Corpo de Bombeiros competente, sem aplicar um limite nacional genérico;
- SPDA depende de avaliação de risco e projeto quando aplicável;
- acessibilidade deve ser confirmada na norma vigente, na legislação e no projeto, sem inserir dimensões de memória;
- *as built* deve refletir o executado e verificado, não uma cópia presumida do projeto executivo;
- SPI/IDP não deve ser convertido diretamente em dias de atraso; o efeito temporal deve ser calculado pela rede do cronograma.

## Estrutura do pacote

```text
civil-skills/
├── README.md
├── LICENSE
└── skills/
    ├── orcamento-obra/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   ├── assets/icon.svg
    │   └── references/fontes-oficiais.md
    ├── cronograma-obra/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   ├── assets/icon.svg
    │   ├── references/metodologias-fontes.md
    │   └── scripts/schedule_math.py
    └── memorial-descritivo-obra/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── assets/icon.svg
        └── references/
            ├── estrutura-modelo.md
            └── fontes-normativas.md
```

## Autoria, licença e origem

Adaptação, revisão técnica e organização desta edição por **Jairo Luz**, com foco em orçamento, projetos, planejamento e gestão de obras no Brasil.

Criada a partir de um fork do repositório: https://github.com/heliopaivajr/civil-skills

O projeto original foi desenvolvido por **Hélio Paiva Jr.** e distribuído sob licença MIT. Ao redistribuir esta adaptação, manter os avisos de autoria, a referência ao projeto original e o arquivo de licença correspondente.

### Alterações desta edição

- conclusão e integração das três skills;
- adaptação para o sistema de Skills do ChatGPT/Codex;
- metadados e ícones para apresentação na interface;
- autoria de Jairo Luz e atribuição ao projeto original;
- referências complementares e critérios de rastreabilidade;
- proteção contra preços, códigos, durações e especificações inventadas;
- tratamento de documentos preliminares, conflitos, linha de base e *as built*;
- atualização da segurança de obra para NR-18 e PGR;
- script de apoio para CPM e EVM em `cronograma-obra`;
- encaminhamento obrigatório entre orçamento, cronograma e memorial.
