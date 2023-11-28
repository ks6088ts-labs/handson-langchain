from pydantic import BaseModel, Field


class SummarizeRequest(BaseModel):
    url: str = Field(description="URL", example="https://www.youtube.com/watch?v=xxxxx")


class SummarizeResponse(BaseModel):
    content: str = Field(description="Summarized content", example="12345")
    cost: float = Field(description="Cost", example=0.12345)
