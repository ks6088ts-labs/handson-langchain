from typing import List

from pydantic import BaseModel, Field


class ChromaBase(BaseModel):
    query: str | None = Field(None, description="クエリ", example="こんにちは")


class ChromaSearchRequest(ChromaBase):
    n_results: int = Field(3, description="検索結果の数", example=3)


class Document(BaseModel):
    class Metadatas(BaseModel):
        source: str
        title: str
        score: float

        class Config:
            extra = "allow"

    text: str
    metadatas: Metadatas


class ChromaSearchResponse(ChromaBase):
    id: str = Field(
        ..., description="メッセージID", example="00000000-0000-0000-0000-000000000000"
    )
    documents: List[Document]
