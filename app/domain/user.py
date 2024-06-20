from typing import Annotated

from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from litestar.dto import DTOConfig

from app.infrastructure.database.repo import BaseRepository
from app.infrastructure.database.service import BaseService
from app.infrastructure.database.tables import User


CreateUser = SQLAlchemyDTO[
    Annotated[
        User,
        DTOConfig(
            exclude={"created_at", "updated_at", "id", "todo"},
        ),
    ]
]

UpdateUser = SQLAlchemyDTO[
    Annotated[
        User,
        DTOConfig(
            exclude={"created_at", "updated_at"},
        ),
    ]
]

class UserRepository(BaseRepository[User]):
    model_type = User


class UserService(BaseService[User]):
    repository_type = UserRepository
