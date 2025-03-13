from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class EventBaseSchema(BaseModel):
    title: str
    start_datetime: datetime
    end_datetime: datetime
    stadium_id: UUID

    class Config:
        from_attributes = True


class EventAddSchema(EventBaseSchema):
    pass


class EventResponseSchema(EventBaseSchema):
    id: UUID
