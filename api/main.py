from fastapi import FastAPI

from api.routers.information import router as information_router

app = FastAPI()

app.include_router(information_router)
# add more routers here
