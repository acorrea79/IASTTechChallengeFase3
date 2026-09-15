# Gold territorial da Fase 2

O notebook `notebooks/01_pipeline_end_to_end.ipynb` materializa:

`phase2_gold_territorial.parquet`

Essa camada é criada a partir da tabela de metas municipais e processada com a
função `add_meta_reference()` versionada no repositório da Fase 2:

`acorrea79/techchallenge-fase2-pipeline-alfabetizacao`

A análise prospectiva 2023→2030 da Fase 3 consome esse Parquet como entrada
territorial.

O arquivo Parquet é gerado durante a execução e não é incluído no Git por padrão.
