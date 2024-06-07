from litestar.plugins.sqlalchemy import SQLAlchemyPlugin

from app.config.app import alchemy


litestar_plugins = [SQLAlchemyPlugin(config=alchemy)]
