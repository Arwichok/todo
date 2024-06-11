from litestar import Router, get
from litestar.response import Redirect

from .todos import WebTodoController

@get("/")
async def redirect() -> Redirect:
    return Redirect("/todos")


router = Router(
    path="/",
    route_handlers=[
        redirect,
        WebTodoController,
    ],
    include_in_schema=False,
)