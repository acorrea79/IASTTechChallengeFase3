# Dados e proveniência

Este repositório não versiona os dados brutos.

## Linhagem da Fase 2

A Fase 3 dá continuidade ao projeto:

`https://github.com/acorrea79/techchallenge-fase2-pipeline-alfabetizacao`

A Fase 2 produziu camadas Gold de indicadores, metas e priorização territorial.
Essas saídas permanecem como referência da camada de inteligência para políticas
públicas.

Como o target solicitado na Fase 3 está no nível do aluno, foi construída uma Gold
ML adicional no nível de registro de aluno a partir da mesma avaliação, preservando
a linhagem e as regras de elegibilidade.

## Gold ML da Fase 3

Execução de referência:

- Shape: **335.551 × 19**
- SHA-256: `3797E0836F04037405F59B3D92B4431E378F45BBBE9B4759C891FC29406E29DC`
- Nulos: **0**
- Duplicados: **0**

## Features finais

Contexto territorial/socioeconômico:

- `rede`
- `sigla_uf`
- `populacao`
- `pib_per_capita`

Contexto operacional da escola na avaliação:

- `escola_total_registros`
- `escola_taxa_presenca`
- `escola_taxa_preenchimento`
- `escola_taxa_elegiveis`
- `escola_qtd_cadernos`
- `municipio_qtd_escolas_avaliacao`
- `escola_participacao_municipio`

A tentativa de integração direta por `id_escola` com o Censo Escolar de 2022 foi
auditada e apresentou **0% de correspondência** em amostra de 20 mil IDs. A integração
não foi forçada.

As features escolares finais não utilizam `alfabetizado`, `proficiencia`, taxa de
alfabetização ou qualquer variável derivada do target.
