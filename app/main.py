
from fastapi import FastAPI
from app.schemas import MessageRequest
from app.services.predictor import predict_message

app = FastAPI(
    title="Spam Detection API",
    description="An API for classifying messages as spam or normal.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Spam Detection API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "spam-detection-api",
    }


@app.post("/messages")
def receive_message(request: MessageRequest):
    result = predict_message(request.message)

    return {
        "message": request.message,
        **result,
    }
