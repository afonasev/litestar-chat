import pytest
from litestar import Litestar
from litestar.testing import AsyncTestClient

from app.api import app


@pytest.fixture()
async def test_client() -> AsyncTestClient[Litestar]:
    return AsyncTestClient(app=app)
