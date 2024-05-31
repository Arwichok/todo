from litestar import Router

from .todo import TodoController


router = Router(
    path="/api",
    route_handlers=[TodoController],
)
