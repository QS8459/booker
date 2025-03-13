from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class BookingBaseSchema(BaseModel):
    title: str
    seat: Optional[str] = None
    event_id: UUID = None

    class Config:
        from_attributes = True


class BookingAddSchema(BookingBaseSchema):
    pass


class BookingResponseSchema(BookingBaseSchema):
    id: UUID