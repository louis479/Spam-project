from pydantic import BaseModel, Field


class MessageRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=5000,
        description="The message to classify as spam or normal",
    )
