from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class AccountBaseSchema(BaseModel):
    email: str
    role: Optional[str | None] = None

    class Config:
        from_attributes = True


class AccountAddSchema(AccountBaseSchema):
    password: str


class AccountResponseSchema(AccountBaseSchema):
    id: UUID

