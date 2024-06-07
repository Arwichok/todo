from app.infrastructure import application
from app.presentation import rest, web

app = application.create(
    route_handlers=[rest.router, web.router],
)
