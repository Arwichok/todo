from dataclasses import dataclass, field
from functools import lru_cache

from environs import Env


env = Env()


@dataclass
class DatabaseSettings:
    url: str = field(
        default_factory=lambda: env("DATABASE_URL", "sqlite+aiosqlite:///db.sqlite3")
    )


@dataclass
class Settings:
    db: DatabaseSettings = field(default_factory=DatabaseSettings)


@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    settings = Settings()
    return settings
