from sqlalchemy import (
    String,
    Enum
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from src.db.models.base import Base
from passlib.hash import pbkdf2_sha256 as sha256
import enum


class Roles(enum.Enum):
    ADMIN:str = "ADMIN"
    USER: str = "USER"
    VENDOR: str = "VENDOR"


class Account(Base):
    __tablename__ = "account"

    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(300), nullable=False)
    role: Mapped[str] = mapped_column(Enum(Roles), default=Roles.USER)

    user: Mapped['User'] = relationship('User', back_populates='account')
    stadium: Mapped['Stadium'] = relationship('Stadium', back_populates='owner')
    event: Mapped['Event'] = relationship('Event', back_populates='account')

    def set_pwd(self, password: str) -> None:
        self.password = sha256.using().hash(password)

    def ver_pwd(self, password: str) -> bool:
        return sha256.verify(password, self.password)


__all__ = "Account"
