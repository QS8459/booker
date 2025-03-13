from pydantic import BaseModel
from uuid import UUID


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str

    class Config:
        from_attributes = True


class UserAddSchema(UserBaseSchema):
    pass


class UserResponseSchema(UserBaseSchema):
    id: UUID


class UserEditSchema(UserBaseSchema):
    pass
