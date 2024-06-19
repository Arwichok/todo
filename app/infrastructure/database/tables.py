from advanced_alchemy.base import orm_registry, UUIDAuditBase
from sqlalchemy.orm import Mapped, mapped_column

__all__ = [
    "Todo",
    "orm_registry",
]


class Todo(UUIDAuditBase):
    name: Mapped[str]
    done: Mapped[bool] = mapped_column(default=False)
