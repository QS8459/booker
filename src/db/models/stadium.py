from sqlalchemy import (
    String,
    ForeignKey,
    Integer,
    DECIMAL
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from src.db.models.base import Base
from uuid import UUID


class Stadium(Base):

    __tablename__ = 'stadium'

    name: Mapped[str] = mapped_column(String(), nullable=True)
    lat: Mapped[str] = mapped_column(String(), nullable=True)
    lon: Mapped[str] = mapped_column(String(), nullable=True)
    address: Mapped[str] = mapped_column(String(), nullable=True)
    city: Mapped[str] = mapped_column(String(), nullable=True)
    country: Mapped[str] = mapped_column(String(), nullable=True)
    zip: Mapped[str] = mapped_column(String(), nullable=True)
    owner_id: Mapped[UUID] = mapped_column(ForeignKey('account.id'), nullable=False)
    seat_rows: Mapped[int] = mapped_column(Integer, nullable=False, default=True)
    seats: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    free_seats: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    one_hour_booking_price: Mapped[float] = mapped_column(DECIMAL(10,2),nullable=True)
    contacts: Mapped[str] = mapped_column(String(15), nullable=True)

    owner: Mapped['Account'] = relationship('Account', foreign_keys=[owner_id])
    event: Mapped['Event'] = relationship('Event', back_populates='stadium')


__all__ = ("Stadium")
