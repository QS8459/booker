from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from typing import Optional


class EventBaseSchema(BaseModel):
    title: str
    start_datetime: Optional[datetime] = Field(default=None)
    end_datetime: Optional[datetime] = Field(default=None)
    stadium_id: UUID

    class Config:
        from_attributes = True


class EventAddSchema(EventBaseSchema):
    pass


class EventResponseSchema(EventBaseSchema):
    id: UUID
