
from pathlib import Path

import joblib


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "spam_classifier.joblib"

model = joblib.load(MODEL_PATH)


def predict_message(message: str) -> dict:
    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]

    confidence = float(max(probabilities))

    return {
        "prediction": str(prediction),
        "confidence": round(confidence, 4),
    }
