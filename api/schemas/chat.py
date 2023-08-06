from pydantic import BaseModel, Field


class ChatBase(BaseModel):
    message: str | None = Field(None, description="チャットメッセージ", example="こんにちは")


class ChatRequest(ChatBase):
    pass


class ChatResponse(ChatBase):
    id: str = Field(
        ..., description="メッセージID", example="00000000-0000-0000-0000-000000000000"
    )
