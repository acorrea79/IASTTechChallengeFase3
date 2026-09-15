# Continuidade técnica com a Fase 2

A Fase 3 continua o repositório:

`https://github.com/acorrea79/techchallenge-fase2-pipeline-alfabetizacao`

## Como a Gold da Fase 2 entra tecnicamente na Fase 3

O notebook principal:

1. clona o repositório da Fase 2;
2. carrega `src/processing/gold_transform.py`;
3. executa diretamente a função `add_meta_reference()`;
4. materializa `data/phase2_gold/phase2_gold_territorial.parquet`;
5. utiliza esse Parquet na análise prospectiva das metas 2030.

Assim, a camada territorial/metas é efetivamente derivada da implementação Gold
da Fase 2.

## Por que existe uma Gold adicional na Fase 3

As Golds territoriais da Fase 2 são agregadas por município/rede e foram
construídas para indicadores, metas e priorização.

O target central da Fase 3 está no nível do aluno. Portanto, é necessária uma
Gold ML adicional no nível de registro de aluno.

Variáveis derivadas do resultado atual, como proficiência, taxa de alfabetização,
distância à meta, status de meta e score de prioridade, não entram como features
do classificador para evitar leakage.
