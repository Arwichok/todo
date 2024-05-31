from litestar import Router

from .todos import TodoController


router = Router(
    path="/api",
    route_handlers=[TodoController],
)
