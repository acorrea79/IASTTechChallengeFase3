# Reprodutibilidade

## Ambiente

A execução de referência foi feita em Google Colab.

O projeto usado para executar jobs do BigQuery pode ser configurado com:

`GCP_PROJECT_ID`

ou:

`GOOGLE_CLOUD_PROJECT`

Na ausência dessas variáveis, o notebook usa `fiap-techchallenge-fase2`.

Um avaliador pode definir um projeto próprio em que possua
`bigquery.jobs.create`; as fontes públicas consultadas não mudam.

## Ordem determinística

A Gold ML é ordenada por:

`ano, id_municipio, id_escola, id_aluno`

antes das etapas estocásticas.

## Notebook executado

A cópia versionada de `notebooks/01_pipeline_end_to_end.ipynb` foi executada
integralmente no Google Colab e preserva os outputs da execução de referência.

Na versão final, as **22 células de código** possuem `execution_count`, há
**48 outputs registrados** e não existem outputs de erro.
