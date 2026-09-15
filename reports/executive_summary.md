# Sumário Executivo

O projeto combina classificação supervisionada, explicabilidade e análise prospectiva
de metas de alfabetização.

O HistGradientBoosting final apresenta PR-AUC de 0,5123 contra 0,4012 do baseline,
e Balanced Accuracy de 0,5649 contra 0,5000. O ganho de F1 é pequeno e é reportado
explicitamente.

A EDA mostra heterogeneidade territorial importante e sustenta as hipóteses usadas
na modelagem. SHAP confirma forte influência da UF, seguida por PIB per capita,
taxa de preenchimento da escola, população e contexto operacional escolar.

Na camada territorial, a Fase 3 consome uma Gold materializada com a implementação
da Fase 2. No cenário tendencial 2030, 2.581 trajetórias município/rede aparecem em
risco; 2.531 possuem score do modelo e podem ser priorizadas.

A solução deve ser usada como apoio à investigação e ao planejamento, não como
diagnóstico automático.
