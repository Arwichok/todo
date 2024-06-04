from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from advanced_alchemy.extensions.litestar import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    async_autocommit_before_send_handler
)

from litestar.template.config import TemplateConfig
from litestar.contrib.jinja import JinjaTemplateEngine

from environs import Env


env = Env()


@dataclass
class DatabaseSettings:
    url: str = field(default_factory=lambda: env("DATABASE_URL"))


@dataclass
class LitestarSettings:
    alchemy: SQLAlchemyAsyncConfig | None
    template: TemplateConfig = field(
        default_factory=lambda: TemplateConfig(
            engine=JinjaTemplateEngine,
            directory=Path(__file__).parent / "presentation/web/templates",
        )
    )


@dataclass
class Settings:
    db: DatabaseSettings = field(default_factory=DatabaseSettings)
    app: LitestarSettings = field(default_factory=LitestarSettings)


@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    settings = Settings()
    settings.app.alchemy = SQLAlchemyAsyncConfig(
        url=settings.db.url,
        before_send=async_autocommit_before_send_handler,
        async_session_config=AsyncSessionConfig(
            expire_on_commit=False
        ),
    )
    return settings

