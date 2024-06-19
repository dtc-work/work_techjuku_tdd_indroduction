from pydantic import BaseModel, Field


class TddRequest(BaseModel):
    question: str = Field("", description="質問")


class TddResponse(BaseModel):
    answer: str = Field("", description="回答")
