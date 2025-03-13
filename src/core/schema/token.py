from pydantic import BaseModel


class TokenBaseSchema(BaseModel):
    access_token: str


class TokenResponseSchema(TokenBaseSchema):
    token_type: str
