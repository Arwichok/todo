from typing import Annotated

from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from litestar.dto import DTOConfig

from app.infrastructure.database.repo import BaseRepository
from app.infrastructure.database.service import BaseService
from app.infrastructure.database.tables import Todo

CreateTodo = SQLAlchemyDTO[
    Annotated[
        Todo,
        DTOConfig(
            exclude={"created_at", "updated_at", "id"},
        ),
    ]
]

UpdateTodo = SQLAlchemyDTO[
    Annotated[
        Todo,
        DTOConfig(
            exclude={"created_at", "updated_at"},
        ),
    ]
]


class TodoRepository(BaseRepository[Todo]):
    model_type = Todo


class TodoService(BaseService[Todo]):
    repository_type = TodoRepository
