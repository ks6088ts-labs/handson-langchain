from pydantic import BaseModel, Field


class SearchBase(BaseModel):
    query: str | None = Field(None, description="クエリ", example="業績")


class SearchRequest(SearchBase):
    pass


class SearchResponse(SearchBase):
    id: str = Field(
        ..., description="トランザクション ID", example="00000000-0000-0000-0000-000000000000"
    )
    result: str = Field(..., description="検索結果", example="検索結果")
