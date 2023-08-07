import uuid

from fastapi import APIRouter
from langchain.retrievers import AzureCognitiveSearchRetriever

from api.schemas import azure_cognitive_search as azure_cognitive_search_schemas
from api.settings import azure_cognitive_search as azure_cognitive_search_settings

settings = azure_cognitive_search_settings.AzureCognitiveSearchSettings()
router = APIRouter()
retriever = AzureCognitiveSearchRetriever(
    service_name=settings.service_name,
    index_name=settings.index_name,
    api_key=settings.api_key,
    content_key="content",
    top_k=1,
)


@router.post(
    "/azure_cognitive_search/search",
    response_model=azure_cognitive_search_schemas.SearchResponse,
)
async def search_index(
    body: azure_cognitive_search_schemas.SearchRequest,
):
    docs = retriever.get_relevant_documents(body.query)
    return azure_cognitive_search_schemas.SearchResponse(
        id=str(uuid.uuid4()),
        result=docs[0].page_content,
    )
