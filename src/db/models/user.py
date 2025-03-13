from sqlalchemy import (
    String,
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from src.db.models.base import Base
from uuid import UUID


class User(Base):
    __tablename__ ="user"

    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    # role: Mapped[Roles] = mapped_column(Enum(Roles), default=Roles.USER, nullable=False)
    account_id: Mapped[UUID] = mapped_column(ForeignKey('account.id'), default=None, nullable=False)

    account: Mapped['Account'] = relationship('Account', foreign_keys=[account_id])


__all__ = ("User")