# Spam Detection API

A FastAPI service that classifies messages as `spam` or `normal` using a
TF-IDF and Naive Bayes model.

## Setup

Create and activate a virtual environment, then install the project
dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

Start the API from the project root:

```bash
uvicorn app.main:app --reload
```

The interactive API documentation is available at `http://127.0.0.1:8000/docs`.
Send a `POST` request to `/messages` with a JSON body such as:

```json
{"message": "Congratulations, you won a prize!"}
```

## Train the model

Training uses `data/messages.csv` and writes the model to
`models/spam_classifier.joblib`:

```bash
python app/train_model.py
```

## Project layout

- `app/`: API, request schema, prediction service, and model-training utilities
- `data/`: labeled message dataset
- `models/`: model artifact loaded by the API
