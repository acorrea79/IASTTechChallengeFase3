# Model Card — HistGradientBoosting

## Finalidade

Classificação de risco em nível de registro de aluno com base em contexto escolar,
territorial e socioeconômico.

O modelo é destinado a triagem e priorização. Não substitui avaliação pedagógica.

## Teste temporal de 2024

| Métrica | Valor |
|---|---:|
| Accuracy | 0,5112 |
| Balanced Accuracy | 0,5649 |
| Precision | 0,4423 |
| Recall | 0,8365 |
| F1 | 0,5786 |
| ROC-AUC | 0,6225 |
| PR-AUC | 0,5123 |

Threshold: **0,31**.

Matriz de confusão: `[[32565, 78493], [12167, 62240]]`.

## Baseline

O Dummy all-risk apresenta:

- F1: 0,5726
- Balanced Accuracy: 0,5000
- PR-AUC: 0,4012

O ganho em F1 é pequeno (+0,0060). Os ganhos mais relevantes são Balanced Accuracy
(+0,0649) e PR-AUC (+0,1111).

## Limitações

- features são principalmente contextuais;
- alunos da mesma escola compartilham contexto;
- poder discriminativo é moderado;
- algumas features escolares são contemporâneas ao ciclo da avaliação;
- a projeção 2030 utiliza apenas dois anos;
- 1,78% das trajetórias prospectivas não possuem score do modelo no recorte usado.
