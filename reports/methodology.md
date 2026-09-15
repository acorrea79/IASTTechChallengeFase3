# Metodologia

## População modelada

Foram mantidos alunos presentes, com caderno preenchido e target conhecido.

O target é `target_nao_alfabetizado`, em que `1` representa não alfabetização.

## Granularidade

A base está no nível de registro de aluno, porém as variáveis explicativas são
contextuais. A primeira versão utilizava somente rede, UF e indicadores municipais,
fazendo alunos do mesmo município/rede receberem vetores praticamente idênticos.

A versão final acrescenta características operacionais da escola, calculadas sem
consultar o target:

- volume de registros da escola;
- taxas de presença e preenchimento;
- taxa de elegibilidade;
- quantidade de cadernos;
- quantidade de escolas avaliadas no município/rede;
- participação da escola no volume municipal.

A cobertura dessas features foi **100%**, e **67,14%** dos grupos município/rede
apresentaram variação entre escolas.

Isso melhora a granularidade contextual, mas não transforma o modelo em diagnóstico
pedagógico individual. Alunos da mesma escola ainda podem compartilhar o mesmo contexto.

## Leakage

Não entram no classificador:

- `alfabetizado` além do papel de target;
- `proficiencia`;
- taxa atual de alfabetização;
- distância para meta;
- status de meta;
- score de prioridade;
- IDs como features.

## Validação

2023 foi utilizado para desenvolvimento, seleção, tuning e definição do threshold.

2024 foi reservado para teste temporal final.

## Seleção de modelo

Foram comparados:

- DummyClassifier;
- Logistic Regression;
- Random Forest;
- HistGradientBoosting.

A seleção/tuning priorizou PR-AUC por representar melhor a capacidade de ordenar risco
sem depender do threshold. O modelo final foi `HistGradientBoosting`.

O threshold final foi definido em previsões out-of-fold de 2023 e ficou em **0,31**.
