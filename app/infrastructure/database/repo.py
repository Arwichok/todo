from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from typing import Any, Generic, Type, TypeVar, Self
from sqlalchemy.ext.asyncio import AsyncSession

M = TypeVar("M")


class BaseRepository(SQLAlchemyAsyncRepository, Generic[M]):
    model_type: Type[M]
    
    @classmethod
    async def provide(cls, db_session: AsyncSession) -> Self:
        return cls(session=db_session)
    