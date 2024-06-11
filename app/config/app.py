from pathlib import Path

from litestar.contrib.jinja import JinjaTemplateEngine
# from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from litestar.template.config import TemplateConfig
from litestar.config.compression import CompressionConfig
from advanced_alchemy.extensions.litestar import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    async_autocommit_before_send_handler
)


from app.config.base import get_settings
from app.config.paths import TEMPLATES_PATH

settings = get_settings()
alchemy = SQLAlchemyAsyncConfig(
    connection_string=settings.db.url,
    before_send_handler=async_autocommit_before_send_handler,
    session_config=AsyncSessionConfig(expire_on_commit=False)
)
template = TemplateConfig(
    engine=JinjaTemplateEngine,
    directory=TEMPLATES_PATH,
)
compression = CompressionConfig(backend="gzip", gzip_compress_level=9)
