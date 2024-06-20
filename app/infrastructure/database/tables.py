from advanced_alchemy.base import orm_registry, UUIDAuditBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

__all__ = [
    "Todo",
    "User",
    "orm_registry",
]


class User(UUIDAuditBase):
    name: Mapped[str]
    todo: Mapped[list["Todo"]] = relationship(back_populates="user")


class Todo(UUIDAuditBase):
    name: Mapped[str]
    done: Mapped[bool] = mapped_column(default=False)
    user: Mapped["User"] = relationship(back_populates="todo")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
