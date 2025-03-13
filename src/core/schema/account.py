from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from src.db.models.account import Roles


class AccountBaseSchema(BaseModel):
    email: str
    role: Optional[str] = Roles.USER.value

    class Config:
        from_attributes = True


class AccountAddSchema(AccountBaseSchema):
    password: str


class AccountResponseSchema(AccountBaseSchema):
    id: UUID

