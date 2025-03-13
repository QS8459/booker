from fastapi import APIRouter
from src.api.v1 import v1

api: APIRouter = APIRouter(prefix="/api")

api.include_router(v1)
