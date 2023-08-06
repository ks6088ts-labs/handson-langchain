from fastapi import FastAPI

from api.routers.chat import router as chat_router
from api.routers.information import router as information_router

app = FastAPI()

app.include_router(information_router)
app.include_router(chat_router)
