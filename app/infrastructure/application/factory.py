from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from litestar import Litestar
    from litestar.types import ControllerRouterHandler


def create(
    *,
    route_handlers: Sequence[ControllerRouterHandler] | None = None,
    **kwargs,
) -> Litestar:
    from litestar import Litestar
    from litestar.contrib.htmx.request import HTMXRequest
    from litestar.di import Provide

    from app.config import app as config
    from app.config import get_settings

    from .plugins import litestar_plugins

    return Litestar(
        route_handlers=route_handlers or [],
        template_config=config.template,
        plugins=litestar_plugins,
        dependencies=dict(
            settings=Provide(get_settings, 0, 1),
        ),
        compression_config=config.compression,
        request_class=HTMXRequest,
        **kwargs,
    )
