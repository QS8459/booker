from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class StadiumBaseSchema(BaseModel):
    name: str
    lat: Optional[str] = None
    lon: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    zip: Optional[str] = None
    seats: Optional[int] = 0
    free_seats: Optional[int] = 0

    class Config:
        from_attributes = True


class StadiumAddSchema(StadiumBaseSchema):
    pass


class StadiumResponseSchema(StadiumBaseSchema):
    id: UUID
