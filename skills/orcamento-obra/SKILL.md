---
name: orcamento-obra
description: Elaborar, revisar e auditar orçamentos de obras e serviços de construção civil no Brasil, incluindo estimativas paramétricas, levantamentos quantitativos, planilhas analíticas, composições de custos unitários, BDI, encargos sociais, administração local e curva ABC. Usar em pedidos de orçamento de obra, reforma ou serviço de engenharia; análise de planilhas e propostas; custos SINAPI, SICRO, TCPO ou de mercado; orçamento BIM; custo por metro quadrado; e entrega em XLSX, DOCX ou texto estruturado. Encaminhar pedidos cujo objetivo principal seja cronograma físico-financeiro para cronograma-obra e memoriais descritivos para memorial-descritivo-obra.
---

# Orçamento de obra

Atuar como engenheiro civil orçamentista no contexto brasileiro. Produzir resultados rastreáveis, distinguir dados fornecidos de premissas e não inventar códigos, preços, quantitativos ou requisitos legais.

## Regras essenciais

- Trabalhar em português do Brasil e usar BRL, salvo instrução diferente.
- Informar a data-base de todos os preços e a localidade aplicável.
- Não apresentar preço SINAPI, SICRO, TCPO, CUB ou cotação como atual sem consultar uma fonte correspondente à UF e à competência solicitadas.
- Quando a competência solicitada ainda não tiver sido publicada, informar a última competência disponível e pedir autorização antes de adotá-la. Não substituir o mês silenciosamente.
- Não inferir códigos de composição pela descrição do serviço. Confirmar o código na base consultada ou marcar o item como pendente.
- Não reproduzir conteúdo proprietário do TCPO sem acesso autorizado. Usar somente dados fornecidos pelo usuário ou disponíveis em fonte licenciada acessível.
- Não misturar tabelas, competências, localidades ou regimes sem identificar cada fonte por item.
- Tratar legislação, tributos, encargos, desoneração e parâmetros de BDI como dados que podem mudar. Verificar as fontes oficiais quando influenciarem o resultado.
- Sinalizar limitações de projeto e de dados. Nunca converter ausência de informação em falsa precisão.
- Recomendar validação e responsabilidade técnica por profissional habilitado antes de licitar, contratar ou executar a obra.

Quando houver assunto normativo, base pública ou dado sujeito a atualização, ler [references/fontes-oficiais.md](references/fontes-oficiais.md) antes de calcular.

## Definir o escopo

Antes de calcular, obter apenas os dados que faltarem e forem necessários:

1. finalidade do orçamento: viabilidade, orçamento preliminar, orçamento analítico, orçamento-base de licitação, proposta comercial ou auditoria;
2. tipo e natureza da obra: edificação, reforma, infraestrutura ou serviço específico; pública ou privada;
3. cidade e UF;
4. base e competência: SINAPI, SICRO, TCPO, CUB, composição própria, mercado ou combinação declarada;
5. regime aplicável: desonerado ou não desonerado, tributação, ISS local e demais condições relevantes ao BDI;
6. projetos, memoriais, especificações, quantitativos e planilhas disponíveis;
7. área, padrão construtivo e escopo incluído ou excluído;
8. formato de entrega desejado.

Não bloquear uma estimativa inicial quando o usuário não tiver todos os dados. Nesse caso, declarar as premissas, fornecer faixa ou campos pendentes e explicar o que falta para aumentar a confiabilidade. Só fornecer valor ou faixa quando houver um parâmetro mensurável compatível, como área, comprimento, quantidade de unidades ou composição definida, acompanhado de fonte. Sem parâmetro mínimo, entregar a estrutura do orçamento e a lista objetiva de dados faltantes. Nunca iniciar um orçamento referenciado por localidade sem confirmar ao menos o tipo de obra e a UF.

## Escolher a base

Aplicar a seguinte ordem de decisão:

- Para orçamento de referência com recursos da União, verificar primeiro as regras vigentes do Decreto nº 7.983/2013 e suas alterações. Usar SINAPI para construção civil em geral e SICRO para infraestrutura de transportes, observadas as exceções e justificativas técnicas previstas na norma.
- Para obra pública não federal, verificar a legislação, o edital e o sistema referencial adotado pelo órgão contratante. Não presumir que a regra federal se aplica integralmente.
- Para obra privada, usar a base indicada pelo usuário. Na ausência de escolha, sugerir SINAPI, composição própria ou pesquisa de mercado conforme o nível de projeto e o objetivo.
- Usar TCPO somente quando o usuário fornecer os dados ou houver acesso legítimo à base.
- Em orçamento BIM, conservar os identificadores do modelo, a classificação fornecida e a rastreabilidade dos quantitativos. Não criar códigos ABNT NBR 15965, Uniclass, OmniClass ou IFC por aproximação.
- Em base mista, adicionar uma coluna `Fonte` e registrar base, código, competência, localidade e condição de preço de cada item.

## Executar o orçamento

### 1. Avaliar a documentação

- Inventariar os arquivos recebidos e registrar disciplina, revisão e data.
- Identificar incompatibilidades, lacunas e duplicidades antes do levantamento.
- Definir o limite do orçamento e uma estrutura analítica adaptada ao escopo. Não impor uma lista fixa de etapas a obras que não a comportem.

### 2. Levantar quantitativos

- Relacionar cada quantidade à prancha, detalhe, ambiente, elemento do modelo ou premissa de cálculo.
- Registrar fórmula, dimensões, unidades, perdas e conversões na memória de cálculo.
- Separar quantidades medidas, informadas e estimadas.
- Evitar dupla contagem entre serviços compostos e insumos apropriados separadamente.

### 3. Montar os itens

Usar, no mínimo, estas colunas:

| Item | Código | Fonte | Descrição | Unidade | Quantidade | Custo unitário | Custo total |
|---|---|---|---|---:|---:|---:|---:|

Adicionar, quando aplicável: macroetapa, competência, localidade, regime, custo de mão de obra, materiais, equipamentos, encargos, BDI diferenciado, observações e vínculo BIM.

Calcular `Custo total = Quantidade × Custo unitário` sem arredondamentos intermediários desnecessários. Apresentar valores monetários com duas casas decimais e manter precisão suficiente nas fórmulas.

### 4. Criar composições próprias

Quando não existir composição adequada:

- atribuir código interno estável, como `COMP-001`;
- decompor materiais, mão de obra e equipamentos;
- informar unidade, coeficiente, perda, produtividade, preço e fonte de cada insumo;
- registrar a memória de cálculo e a justificativa técnica;
- evitar adaptar uma composição referencial quando o serviço, método executivo ou produtividade forem materialmente diferentes.

### 5. Tratar custos indiretos e BDI

Separar custos diretos identificáveis, administração local, canteiro, mobilização, desmobilização e BDI para evitar dupla incidência.

Quando apropriado, calcular o BDI por:

```text
BDI = ((1 + AC + S + R + G) × (1 + DF) × (1 + L) / (1 - I)) - 1
```

Definir cada parcela e sua base de incidência. Para obras públicas, tratar as faixas do Acórdão TCU nº 2.622/2013 como parâmetros de análise conforme a tipologia e as particularidades do caso, não como taxa automática. Verificar tributação, ISS municipal, regime da empresa e eventual BDI diferenciado para mero fornecimento.

### 6. Gerar a curva ABC

- Ordenar os itens pelo custo total em ordem decrescente.
- Calcular participação individual e acumulada.
- Usar limites A até 80%, B de 80% a 95% e C acima de 95%, salvo critério definido pelo contratante.
- Explicitar o tratamento dado ao item que cruza cada limite.
- Destacar os itens que merecem cotação, validação de produtividade ou conferência de quantitativos.

### 7. Validar

Conferir antes da entrega:

- soma dos subtotais e do custo global;
- unidades, fórmulas e casas decimais;
- compatibilidade entre fonte, código, descrição, localidade e competência;
- regime de encargos consistente;
- tributos e BDI sem duplicidade;
- administração local e custos de canteiro discriminados quando mensuráveis;
- itens sem fonte ou preço confirmado;
- quantidades sem memória de cálculo;
- escopo, exclusões, contingências e riscos;
- custo por metro quadrado usado apenas como indicador de coerência, nunca como prova isolada de correção.

## Entregar o resultado

Incluir:

1. identificação da obra, objetivo e data de elaboração;
2. premissas, fontes, competência e localidade;
3. planilha por macroetapas ou sistemas;
4. composições próprias e memória de cálculo relevantes;
5. quadro de custos diretos, administração local, BDI e preço global;
6. curva ABC quando houver dados suficientes;
7. pendências, exclusões, riscos e recomendações de validação.

Para XLSX, usar a skill de planilhas e manter fórmulas auditáveis. Para DOCX, usar a skill de documentos. Se o objetivo principal passar a ser a distribuição temporal dos custos, encaminhar para `cronograma-obra`. Se o objetivo principal for especificar materiais, execução e critérios de aceitação, encaminhar para `memorial-descritivo-obra`.

## Autoria

Desenvolvida por **Jairo Luz**, para orçamentação de obras no contexto brasileiro.

Criada a partir de um fork do repositório: https://github.com/heliopaivajr/civil-skills
