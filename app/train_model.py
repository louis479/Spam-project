
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


# Define project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "messages.csv"
MODEL_DIR = PROJECT_ROOT / "models"
MODEL_PATH = MODEL_DIR / "spam_classifier.joblib"


# Load the dataset
df = pd.read_csv(DATA_PATH)

# Basic data validation
if df.empty:
    raise ValueError("The dataset is empty.")

if df[["message", "label"]].isnull().any().any():
    raise ValueError("The dataset contains missing messages or labels.")

if set(df["label"].unique()) != {"spam", "normal"}:
    raise ValueError("Labels must be 'spam' and 'normal'.")


# Create the machine-learning pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB()),
])


# Train the model
model.fit(df["message"], df["label"])


# Save the trained model
MODEL_DIR.mkdir(parents=True, exist_ok=True)
joblib.dump(model, MODEL_PATH)

print(f"Training examples: {len(df)}")
print(f"Labels learned: {sorted(df['label'].unique())}")
print(f"Model saved to: {MODEL_PATH}")
