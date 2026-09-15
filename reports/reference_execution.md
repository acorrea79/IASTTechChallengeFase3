# Execução de referência — versão final

## Gold ML

- Shape: 335.551 × 19
- Nulos: 0
- Duplicados: 0
- Cobertura das features escolares operacionais: 100%
- Grupos município/rede com variação entre escolas: 67,15%
- Escolas distintas em 2023: 33.265
- Escolas distintas em 2024: 38.738

## EDA

- target não alfabetizado: 41,72% em 2023 e 40,12% em 2024;
- Norte: maior taxa regional em 2023 e 2024;
- análises de rede, UF, distribuições, outliers, correlações e contexto escolar precedem a modelagem;
- três hipóteses analíticas são registradas no notebook antes da seleção de modelos.

## Modelo

Modelo final: `HistGradientBoosting`

Melhor PR-AUC em CV/tuning de 2023: **0,5722**.

Threshold OOF: **0,31**.

## Teste temporal 2024

| Métrica | Dummy all-risk | Modelo final |
|---|---:|---:|
| Accuracy | 0,4012 | 0,5112 |
| Balanced Accuracy | 0,5000 | 0,5649 |
| Precision | 0,4012 | 0,4423 |
| Recall | 1,0000 | 0,8365 |
| F1 | 0,5726 | 0,5786 |
| ROC-AUC | 0,5000 | 0,6225 |
| PR-AUC | 0,4012 | 0,5123 |

Matriz de confusão:

`[[32565, 78493], [12167, 62240]]`

Ganhos sobre o baseline:

- Δ F1: +0,0060
- Δ Balanced Accuracy: +0,0649
- Δ PR-AUC: +0,1111

## Continuidade com a Fase 2

O notebook clona o repositório da Fase 2, carrega diretamente
`src/processing/gold_transform.py`, aplica `add_meta_reference()` e materializa
`phase2_gold_territorial.parquet`.

A análise prospectiva lê essa Gold materializada.

Execução observada da Gold territorial:

- 10.704 linhas;
- cobertura da meta 2030: 100%.

## Análise prospectiva 2030

Meta oficial auditada: **80%**.

Trajetórias em risco no cenário tendencial: **2.581**.

Após normalização da chave de rede:

- cobertura com score do modelo: **98,22%**;
- trajetórias em risco com score disponível e priorizáveis: **2.531**;
- 50 trajetórias em risco não receberam score no recorte modelado e não entram no ranking.

A projeção utiliza apenas 2023 e 2024, sendo apresentada como cenário exploratório,
não como forecast formal de série temporal.
