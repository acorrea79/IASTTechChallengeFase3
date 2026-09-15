# EDA — principais achados da execução de referência

A modelagem é precedida por análise exploratória no notebook principal.

## Distribuição do target

| Ano | Alfabetizado | Não alfabetizado |
|---:|---:|---:|
| 2023 | 58,28% | 41,72% |
| 2024 | 59,88% | 40,12% |

Há leve melhora agregada entre 2023 e 2024.

## Risco por rede

Em 2023, a taxa de não alfabetização foi aproximadamente:

- Estadual: 38,60%
- Municipal: 42,03%

Em 2024:

- Estadual: 37,45%
- Municipal: 40,52%

A rede privada possui amostra residual no recorte de 2024 e não é interpretada
como evidência comparável.

## Risco por região

| Região | 2023 | 2024 |
|---|---:|---:|
| Centro-Oeste | 41,42% | 35,81% |
| Nordeste | 45,53% | 42,85% |
| Norte | 48,75% | 49,18% |
| Sudeste | 40,89% | 37,61% |
| Sul | 32,33% | 38,94% |

O Norte apresenta a maior taxa nos dois anos. A diferença regional reforça a
hipótese de forte componente territorial.

## Hipóteses usadas na modelagem

1. **Heterogeneidade territorial:** UF deve contribuir para ordenar risco.
2. **Variação escolar:** características operacionais da escola adicionam
   informação além do município/rede.
3. **Não linearidade:** população, PIB per capita e contexto escolar podem ter
   relações não lineares com o target, justificando comparar modelos lineares
   e baseados em árvores/boosting.

O notebook também gera distribuições numéricas, análise de outliers,
correlações exploratórias e perfis de contexto escolar antes da modelagem.
