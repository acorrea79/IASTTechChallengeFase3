# Limitações e possíveis evoluções futuras

## Limitações

1. O target é individual, mas as features são majoritariamente contextuais.
2. Alunos da mesma escola compartilham parte relevante do vetor de entrada.
3. As features escolares operacionais são contemporâneas ao ciclo de avaliação.
4. O ganho de F1 sobre o baseline all-risk é pequeno.
5. ROC-AUC permanece moderado.
6. A chave `id_escola` da avaliação não apresentou correspondência direta com o Censo
   Escolar de 2022, impedindo enriquecimento externo por escola sem uma tabela de ponte.
7. A projeção 2030 utiliza apenas dois anos observados.
8. Alguns itens do ranking prospectivo possuem amostras reduzidas.

## Possíveis evoluções futuras

- obter uma tabela oficial de correspondência entre IDs de escola;
- incorporar atributos pedagógicos individuais pré-avaliação, se disponíveis sem leakage;
- construir features escolares de ano anterior para uma aplicação estritamente ex-ante;
- ampliar a série histórica e comparar modelos temporais formais;
- calibrar probabilidades;
- otimizar threshold por custo de política pública;
- avaliar estabilidade e fairness por região, rede e porte municipal;
- validar o pipeline em novos anos;
- disponibilizar painel de acompanhamento das trajetórias de meta.
