from app.infrastructure import application

from app.presentation import rest


app = application.create(
    route_handlers=[
        rest.router
    ],
)
