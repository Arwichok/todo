from advanced_alchemy.base import orm_registry, UUIDAuditBase
from sqlalchemy.orm import Mapped, mapped_column, MappedAsDataclass
# from litestar.contrib.sqlalchemy.base import UUIDAuditBase


class Todo(UUIDAuditBase):
    name: Mapped[str]
    done: Mapped[bool] = mapped_column(default=False)
