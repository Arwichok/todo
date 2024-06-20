from uuid import UUID
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
    todo: Mapped[list["Todo"]] = relationship(back_populates="user", lazy="selectin")


class Todo(UUIDAuditBase):
    name: Mapped[str]
    done: Mapped[bool] = mapped_column(default=False)
    user: Mapped["User"] = relationship(lazy="joined", innerjoin=True, viewonly=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
