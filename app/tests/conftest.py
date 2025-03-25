import pytest
from sqlalchemy.ext.asyncio import create_async_engine
from fastapi.testclient import TestClient
from typing import Generator, AsyncGenerator
from httpx import AsyncClient

from src.core.config import settings
from src.core.database import Base
from src.main import app

TEST_DATABASE_URL = settings.DATABASE_URL

@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)

@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        yield ac

@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    assert settings.MODE =="TEST"
    if settings.MODE == "TEST":
        engine = create_async_engine(TEST_DATABASE_URL, echo=True)

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        yield

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)