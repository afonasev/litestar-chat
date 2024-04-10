from litestar import Litestar
from litestar.status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from litestar.testing import AsyncTestClient


async def test_get_users(
    test_client: AsyncTestClient[Litestar],
) -> None:
    async with test_client as client:
        response = await client.get("/users")
        assert response.status_code == HTTP_200_OK
        assert response.json() == []


async def test_create_user(
    test_client: AsyncTestClient[Litestar],
) -> None:
    user = {
        "id": 1,
        "last_name": "last_name",
        "first_name": "first_name",
    }
    async with test_client as client:
        response = await client.post(
            "/users",
            json=user,
        )
        assert response.status_code == HTTP_201_CREATED
        assert response.json() == user


async def test_get_user(
    test_client: AsyncTestClient[Litestar],
) -> None:
    async with test_client as client:
        response = await client.get(
            "/users/3",
        )
        assert response.status_code == HTTP_200_OK
        assert response.json() == {
            "id": 3,
            "last_name": "last_name",
            "first_name": "first_name",
        }


async def test_get_not_existed_user(
    test_client: AsyncTestClient[Litestar],
) -> None:
    async with test_client as client:
        response = await client.get(
            "/users/0",
        )
        assert response.status_code == HTTP_404_NOT_FOUND


async def test_update_user(
    test_client: AsyncTestClient[Litestar],
) -> None:
    user = {
        "id": 1,
        "last_name": "last_name",
        "first_name": "first_name",
    }
    async with test_client as client:
        response = await client.put(
            "/users/1",
            json=user,
        )
        assert response.status_code == HTTP_200_OK
        assert response.json() == user
