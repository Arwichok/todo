from typing import Any, Generic, Self

from advanced_alchemy import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession
from .repo import BaseRepository, M


class BaseService(SQLAlchemyAsyncRepositoryService, Generic[M]):
    repository_type: type[BaseRepository[M]]

    @classmethod
    async def provide(cls, db_session: AsyncSession) -> Self:
        return cls(session=db_session)