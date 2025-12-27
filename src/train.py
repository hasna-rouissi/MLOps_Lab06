from __future__ import annotations

"""
Module d'entraînement et d'enregistrement d'un modèle de churn.

Ce script :
1. Charge le jeu de données prétraité `data/processed.csv`
2. Sépare les variables explicatives (features) de la cible `churn`
3. Définit un pipeline scikit-learn :
   - prétraitement (StandardScaler + OneHotEncoder)
   - modèle de régression logistique
4. Coupe les données en train / test
5. Entraîne le modèle et calcule les métriques
6. Compare la F1 à une baseline triviale
7. Sauvegarde :
   - le modèle versionné dans `models/`
   - un alias stable `models/model.joblib` (pour DVC)
   - les métadonnées dans `registry/metadata.json`
   - le fichier `registry/current_model.txt` si le gate est validé
"""

from datetime import datetime
from pathlib import Path
from typing import Any, Final
import json

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# ---------------------------------------------------------------------------
# Chemins et constantes
# ---------------------------------------------------------------------------

ROOT: Final[Path] = Path(__file__).resolve().parents[1]
DATA_PATH: Final[Path] = ROOT / "data" / "processed.csv"
MODELS_DIR: Final[Path] = ROOT / "models"
REGISTRY_DIR: Final[Path] = ROOT / "registry"
CURRENT_MODEL_PATH: Final[Path] = REGISTRY_DIR / "current_model.txt"
METADATA_PATH: Final[Path] = REGISTRY_DIR / "metadata.json"

# ---------------------------------------------------------------------------
# Gestion des métadonnées
# ---------------------------------------------------------------------------


def load_metadata() -> list[dict[str, Any]]:
    """Charge les métadonnées existantes (ou liste vide)."""
    if not METADATA_PATH.exists():
        return []

    with METADATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_metadata(items: list[dict[str, Any]]) -> None:
    """Sauvegarde les métadonnées des modèles."""
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
    with METADATA_PATH.open("w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)


# ---------------------------------------------------------------------------
# Fonctions utilitaires
# ---------------------------------------------------------------------------


def compute_baseline_f1(y_true: pd.Series | list[int]) -> float:
    """Baseline : prédire toujours 0."""
    y_pred = [0] * len(y_true)
    return float(f1_score(y_true, y_pred, zero_division=0))


def build_preprocessing_pipeline(
    numeric_cols: list[str],
    categorical_cols: list[str],
) -> ColumnTransformer:
    """Pipeline de prétraitement."""
    numeric_transformer = Pipeline(
        steps=[("scaler", StandardScaler())]
    )

    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    return ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_cols),
            ("cat", categorical_transformer, categorical_cols),
        ]
    )


def build_model_pipeline(
    preprocessor: ColumnTransformer,
    seed: int,
) -> Pipeline:
    """Pipeline complet (prétraitement + modèle)."""
    classifier = LogisticRegression(
        max_iter=200,
        random_state=seed,
    )

    return Pipeline(
        steps=[
            ("prep", preprocessor),
            ("clf", classifier),
        ]
    )


# ---------------------------------------------------------------------------
# Fonction principale
# ---------------------------------------------------------------------------


def main(version: str = "v1", seed: int = 42, gate_f1: float = 0.70) -> None:
    """Entraînement, évaluation et enregistrement du modèle."""

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            "Fichier processed.csv introuvable. "
            "Veuillez exécuter l'étape prepare."
        )

    # Chargement des données
    df = pd.read_csv(DATA_PATH)

    target_col = "churn"
    X = df.drop(columns=[target_col])
    y = df[target_col].astype(int)

    numeric_cols = ["tenure_months", "num_complaints", "avg_session_minutes"]
    categorical_cols = ["plan_type", "region"]

    # Pipeline
    preprocessor = build_preprocessing_pipeline(
        numeric_cols=numeric_cols,
        categorical_cols=categorical_cols,
    )
    model_pipeline = build_model_pipeline(preprocessor, seed)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=seed,
        stratify=y,
    )

    # Entraînement
    model_pipeline.fit(X_train, y_train)

    # Évaluation
    y_pred = model_pipeline.predict(X_test)

    metrics = {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, zero_division=0)),
        "f1": float(f1_score(y_test, y_pred, zero_division=0)),
        "baseline_f1": compute_baseline_f1(y_test),
    }

    # Sauvegarde du modèle versionné
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    model_filename = f"churn_model_{version}_{timestamp}.joblib"
    model_path = MODELS_DIR / model_filename
    joblib.dump(model_pipeline, model_path)

    # Métadonnées
    entry: dict[str, Any] = {
        "model_file": model_filename,
        "version": version,
        "trained_at_utc": timestamp,
        "data_file": DATA_PATH.name,
        "seed": seed,
        "metrics": metrics,
        "gate_f1": gate_f1,
        "passed_gate": bool(
            metrics["f1"] >= gate_f1
            and metrics["f1"] >= metrics["baseline_f1"]
        ),
    }

    items = load_metadata()
    items.append(entry)
    save_metadata(items)

    print("[METRICS]", json.dumps(metrics, indent=2))
    print(f"[OK] Modèle sauvegardé : {model_path}")

    # -------------------------------------------------------------------
    # REGISTRY + ALIAS STABLE (POINT CLÉ POUR DVC)
    # -------------------------------------------------------------------

    # Logique de "registry" minimal : mise à jour du modèle courant
    if entry["passed_gate"]:
        REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
        CURRENT_MODEL_PATH.write_text(
            model_filename,
            encoding="utf-8",
        )

        # Alias stable pour DVC
        stable_model_path = MODELS_DIR / "model.joblib"
        joblib.dump(model_pipeline, stable_model_path)

        print(f"[DEPLOY] Modèle activé : {model_filename}")
        print(f"[DEPLOY] Alias stable créé : {stable_model_path}")
    else:
        print(
            "[DEPLOY] Refusé : F1 insuffisante "
            "ou baseline non battue."
        )

        
if __name__ == "__main__":
    main()
