from fastapi import APIRouter

from api.settings import information

settings = information.InformationSettings()
router = APIRouter()


@router.get("/information")
async def get_information():
    return {
        "version": settings.version,
        "revision": settings.revision,
    }
