import uuid

from fastapi import APIRouter
from langchain import LLMMathChain
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

from api.schemas import chat as chat_schemas
from api.settings import chat as chat_settings

settings = chat_settings.ChatSettings()
router = APIRouter()


def create_agent():
    llm = ChatOpenAI(
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
    tools = [
        Tool(
            name="Calculator",
            func=LLMMathChain.from_llm(llm=llm, verbose=True).run,
            description="数理計算の結果を返します",
        ),
    ]

    return initialize_agent(
        tools=tools, llm=llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True
    )


@router.post("/chat", response_model=chat_schemas.ChatResponse)
async def create_task(body: chat_schemas.ChatRequest):
    agent = create_agent()
    response = agent.run(body.message)
    return chat_schemas.ChatResponse(
        id=str(uuid.uuid4()),
        message=response,
    )
