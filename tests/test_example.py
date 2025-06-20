import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """Test the health check endpoint."""
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@pytest.mark.asyncio
async def test_get_examples(client: AsyncClient):
    """Test the get_examples endpoint."""
    # This test assumes you've mocked the database query or seeded test data
    response = await client.get("/api/v1/examples", params={"page": 1, "page_size": 10})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "total" in data
    assert "page" in data
    assert "page_size" in data
    assert "pages" in data
    assert "items" in data