from sqlalchemy import (
    ForeignKey,
    String,
    Integer
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from src.db.models.base import Base
from uuid import UUID


class Booking(Base):
    __tablename__ = "booking"

    title: Mapped[str] = mapped_column(String(), nullable=True)
    seat: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    event_id: Mapped[UUID] = mapped_column(ForeignKey('event.id'), nullable=True)
    account_id: Mapped[UUID] = mapped_column(ForeignKey('account.id'), nullable=True)

    event: Mapped["Event"] = relationship('Event', foreign_keys=[event_id])
    account: Mapped['Account'] = relationship('Account', foreign_keys=[account_id])


__all__ = "Booking"
