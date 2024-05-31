from typing import Sequence
from litestar import Litestar
from litestar.types import ControllerRouterHandler



def create(
        *,
        route_handlers: Sequence[ControllerRouterHandler] | None = None,
        **kwargs,
) -> Litestar:

    return Litestar(
        route_handlers=route_handlers or [],
        **kwargs
    )
