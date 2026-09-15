CATEGORICAL_FEATURES = [
    "rede",
    "sigla_uf",
]

NUMERIC_FEATURES = [
    "populacao",
    "pib_per_capita",
    "escola_total_registros",
    "escola_taxa_presenca",
    "escola_taxa_preenchimento",
    "escola_taxa_elegiveis",
    "escola_qtd_cadernos",
    "municipio_qtd_escolas_avaliacao",
    "escola_participacao_municipio",
]

FEATURES = CATEGORICAL_FEATURES + NUMERIC_FEATURES

SORT_KEY = [
    "ano",
    "id_municipio",
    "id_escola",
    "id_aluno",
]
