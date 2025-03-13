from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import (
    String,
    Uuid,
    DateTime,
    Enum
)
from datetime import datetime
from uuid import uuid4, UUID
import enum


class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, nullable=False, default=uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"

    def __str__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"
