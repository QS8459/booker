from fastapi import APIRouter
from src.api.v1.account import account
from src.api.v1.stadium import stadium
from src.api.v1.user import user
from src.api.v1.event import event
from src.api.v1.booking import booking

v1: APIRouter = APIRouter(prefix="/v1")

v1.include_router(user)
v1.include_router(event)
v1.include_router(stadium)
v1.include_router(account)
v1.include_router(booking)
