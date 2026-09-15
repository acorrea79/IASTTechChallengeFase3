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

Para a submissão final, deve ser versionada a cópia do notebook baixada
diretamente do Colab após `Executar tudo`, preservando os outputs.
