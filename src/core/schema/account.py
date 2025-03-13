from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class AccountBaseSchema(BaseModel):
    email: str

    class Config:
        from_attributes = True


class AccountCreateSchema(AccountBaseSchema):
    password: str


class AccountResponseSchema(AccountBaseSchema):
    id: UUID
    role: Optional[str | None] = None

