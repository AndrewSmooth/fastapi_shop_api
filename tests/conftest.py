import asyncio

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine
from fastapi.testclient import TestClient

from src.core.config import settings
from src.core.database import Base, DATABASE_URL
from src.main import app

TEST_DATABASE_URL = DATABASE_URL

@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()

@pytest.fixture(scope="session")
def client():
    return TestClient(app)

@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    if settings.db.MODE == "TEST":
        engine = create_async_engine(TEST_DATABASE_URL, echo=True)

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        yield

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)