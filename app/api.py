import logging
from dataclasses import dataclass

from litestar import Controller, Litestar, get, post
from litestar.exceptions import NotFoundException
from litestar.types import Scope
from structlog import get_logger

from app.tools.logging import configure_logging

logger = get_logger()
logger_std = logging.getLogger()


@dataclass
class User:
    id: int
    first_name: str
    last_name: str


class UserController(Controller):
    path = "/users"

    @post()
    async def create_user(self, data: User) -> User:
        logger.info("User created", user=data)
        return data

    @get()
    async def list_users(self) -> list[User]:
        return []

    @get(path="/{user_id:int}")
    async def get_user(self, user_id: int) -> User:
        if user_id == 0:
            raise NotFoundException
        return User(id=user_id, first_name="first_name", last_name="last_name")


async def exception_handler(exc: Exception, scope: Scope) -> None:
    logger.exception(
        "Unexpected error",
        exc=type(exc).__name__,
        message=str(exc),
        path=scope["path"],
    )


def create_app() -> Litestar:
    app = Litestar(
        [UserController],
        after_exception=[exception_handler],
    )
    configure_logging()
    return app


app = create_app()
