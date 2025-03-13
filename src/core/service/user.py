from typing import Type

from fastapi import Depends

from src.core.base import BaseService, T
from src.db.models.user import User
from src.db.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


class UserService(BaseService):

    def __init__(self, session: AsyncSession):
        super().__init__(session, User)

    async def before_add(self, instance: Type[T] = None, *args, **kwargs):
        pass


def get_user_service(session: AsyncSession = Depends(get_async_session)):
    return UserService(session)
