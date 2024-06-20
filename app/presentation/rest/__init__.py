from litestar import Router

from .todos import TodoController
from .user import UserController


router = Router(
    path="/api",
    route_handlers=[
        TodoController,
        UserController,
    ],
)
