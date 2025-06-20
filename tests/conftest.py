import asyncio
from typing import AsyncGenerator, Generator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from application.application import create_app
from utils.database import get_db_session


# Test database URL - use an in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Create an instance of the default event loop for each test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_db_engine():
    """Create a test database engine."""
    engine = create_async_engine(
        TEST_DATABASE_URL,
        echo=False,
        future=True,
    )
    
    # Create tables
    # await init_db(engine)  # Uncomment and implement this function to create tables
    
    yield engine
    
    # Drop tables
    # await drop_db(engine)  # Uncomment and implement this function to drop tables


@pytest.fixture
async def test_db_session(test_db_engine) -> AsyncGenerator[AsyncSession, None]:
    """Create a test database session."""
    async_session = sessionmaker(
        test_db_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
    )
    
    async with async_session() as session:
        yield session


@pytest.fixture
async def app(test_db_session) -> FastAPI:
    """Create a test FastAPI app."""
    app = create_app()
    
    # Override database dependency
    async def get_test_db_session():
        yield test_db_session
    
    app.dependency_overrides[get_db_session] = get_test_db_session
    
    return app


@pytest.fixture
async def client(app) -> AsyncGenerator[AsyncClient, None]:
    """Create a test HTTP client."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client