
from fastapi import FastAPI
from app.schemas import MessageRequest

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
    return {
        "message": request.message,
        "status": "Message received successfully",
    }

