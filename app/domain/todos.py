from dataclasses import dataclass
from uuid import UUID
from app.infrastructure.database.tables import Todo
from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from app.infrastructure.database.repo import BaseRepository
from app.infrastructure.database.service import BaseService
from litestar.dto import DTOConfig
from typing import Annotated
from msgspec import Struct, convert
from litestar.dto import DTOConfig, MsgspecDTO, DataclassDTO

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService


CreateTodoDTO = SQLAlchemyDTO[Annotated[Todo, DTOConfig(
    exclude={"created_at", "updated_at", "id"},
)]]

ChangeTodoDTO = SQLAlchemyDTO[Annotated[Todo, DTOConfig(
    exclude={"created_at", "updated_at"},
)]]


class TodoRepository(BaseRepository[Todo]):
    model_type = Todo


class TodoService(BaseService[Todo]):
    repository_type = TodoRepository
