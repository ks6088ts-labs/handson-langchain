import os

from fastapi import FastAPI

from api.routers.azure_cognitive_search import router as azure_cognitive_search_router
from api.routers.chat import router as chat_router
from api.routers.chroma import router as chroma_router
from api.routers.information import router as information_router

from .helper_langserve import add_langserve_routes

app = FastAPI(
    title="handson-langchain API server",
    description="handson-langchain API server using FastAPI",
)

DEBUG = str(os.getenv("DEBUG")).lower() == "true"

if DEBUG:
    add_langserve_routes(app=app)

app.include_router(information_router)
app.include_router(chat_router)
app.include_router(azure_cognitive_search_router)
app.include_router(chroma_router)
