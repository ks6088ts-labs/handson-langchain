import logging

import pytest
import pytest_asyncio
import starlette.status
from httpx import AsyncClient

from api.main import app


@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_information(async_client):
    response = await async_client.get("/information")
    assert response.status_code == starlette.status.HTTP_200_OK
    logging.info(response.json())


@pytest.mark.skip(reason="Don't want to consume OpenAI API quota")
@pytest.mark.asyncio
async def test_chat(async_client):
    response = await async_client.post("/chat", json={"message": "Hello World!"})
    assert response.status_code == starlette.status.HTTP_200_OK
    logging.info(response.json())
