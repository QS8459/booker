from sqlalchemy import (
    String,
    ForeignKey,
    DateTime,
    Uuid
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from src.db.models.base import Base
from datetime import datetime
from uuid import UUID


class Event(Base):
    __tablename__ = "event"

    title: Mapped[str] = mapped_column(String, nullable=True)
    start_datetime: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end_datetime: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    stadium_id: Mapped[UUID] = mapped_column(ForeignKey('stadium.id'), nullable=False)
    account_id: Mapped[UUID] = mapped_column(ForeignKey('account.id'), nullable=False)

    stadium: Mapped['Stadium'] = relationship("Stadium", foreign_keys=[stadium_id])
    account: Mapped['Account'] = relationship('Account', foreign_keys=[account_id])


__all__ = "Event"