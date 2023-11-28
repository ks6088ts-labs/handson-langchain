from fastapi import APIRouter
from langchain.callbacks import get_openai_callback
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import YoutubeLoader
from langchain.prompts import PromptTemplate

from api.schemas import youtube as youtube_schemas
from api.settings import youtube as youtube_settings

settings = youtube_settings.YouTubeSettings()
router = APIRouter()

PROMPT_TEMPLATE = """Write a concise Japanese summary of the following transcript of Youtube Video.
============

{text}

============

日本語で 500 文字以内で要約した結果は以下の通りです。
"""


def create_llm():
    return ChatOpenAI(
        model_name=settings.openai_model_name,
        openai_api_base=settings.openai_api_base,
        openai_api_key=settings.openai_api_key,
        temperature=0,
        model_kwargs={
            "deployment_id": settings.openai_deployment_id,
            "api_type": settings.openai_api_type,
            "api_version": settings.openai_api_version,
        },
    )


def get_documents(url):
    return YoutubeLoader.from_youtube_url(
        url, add_video_info=True, language=["en", "ja"]
    ).load()


def get_summary(llm, docs):
    with get_openai_callback() as cb:
        chain = load_summarize_chain(
            llm,
            chain_type="stuff",
            verbose=False,
            prompt=PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["text"]),
        )
        response = chain({"input_documents": docs}, return_only_outputs=True)
    return response["output_text"], cb.total_cost


@router.post("/youtube/summarize", response_model=youtube_schemas.SummarizeResponse)
async def chat(body: youtube_schemas.SummarizeRequest):
    llm = create_llm()
    docs = get_documents(body.url)
    summary, cost = get_summary(llm, docs)

    return youtube_schemas.SummarizeResponse(
        content=summary,
        cost=cost,
    )
