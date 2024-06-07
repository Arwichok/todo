from litestar import Router

from .todos import WebTodoController

router = Router(
    path="/",
    route_handlers=[
        WebTodoController,
    ],
)