from typing import Type

from fastapi import Depends, HTTPException

from src.core.base import BaseService, T
from src.db.models.account import Account
from src.db.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class AccountService(BaseService):

    def __init__(self, session: AsyncSession):
        super().__init__(session, Account)

    async def before_add(self, instance: Type[T] = None, *args, **kwargs):
        instance.set_pwd(kwargs.get('password'))

    async def get_by_email(self, email: str):
        async def _get_by_email(in_email: str):
            query = select(self.model).where(self.model.email == in_email)
            return await self.session.execute(query)

        return await self._exec(_get_by_email, in_email=email, fetch_one=True)

    async def authenticate(self, email: str, password: str):
        user = await self.get_by_email(email)
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="Wrong Email or Password"
            )
        if user.ver_pwd(password):
            return {
                "email": user.email,
                'id': user.id,
                'role': user.role.value
            }
        else:
            raise HTTPException(
                status_code=404,
                detail="Wrong Email or Password"
            )


def get_account_service(session: AsyncSession = Depends(get_async_session)):
    return AccountService(session)
