from scipy.stats import loguniform, randint
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline

from src.preprocessing.pipeline import build_preprocessor

RANDOM_STATE = 42
FINAL_THRESHOLD = 0.31

def build_search():
    pipeline = Pipeline([
        ("preprocessor", build_preprocessor()),
        ("model", HistGradientBoostingClassifier(random_state=RANDOM_STATE)),
    ])

    params = {
        "model__learning_rate": loguniform(0.03, 0.15),
        "model__max_iter": randint(120, 241),
        "model__max_leaf_nodes": [15, 31, 63],
        "model__min_samples_leaf": [10, 20, 40],
        "model__l2_regularization": loguniform(1e-4, 2.0),
    }

    cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=RANDOM_STATE)

    return RandomizedSearchCV(
        pipeline,
        params,
        n_iter=10,
        scoring="average_precision",
        cv=cv,
        random_state=RANDOM_STATE,
        n_jobs=-1,
        refit=True,
    )
