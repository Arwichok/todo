from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from app.infrastructure.database.tables import Todo
from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO


TodoDTO = SQLAlchemyDTO[Todo]


class TodoRepository(SQLAlchemyAsyncRepository[Todo]):
    model_type = Todo
