from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generic, TypeVar, Type
from abc import ABC, abstractmethod
from sqlalchemy.future import select
from sqlalchemy import func
from uuid import UUID
from fastapi import HTTPException, status

from src.conf.log import logger

T = TypeVar("T")


class BaseService(ABC, Generic[T]):

    def __init__(self, session: AsyncSession, model: Type[T]):
        self.session = session
        self.model = model

    async def __handle_in_session(self, call_next, refresh=False, *args, **kwargs):
        try:
            result = await call_next(*args, **kwargs)
            await self.session.commit()
            if refresh:
                await self.session.refresh(result)
                return result
            return result
        except Exception as e:
            raise e

    async def _exec(self, call_next, fetch_one: bool = False, refresh: bool = False, update=False, *args, **kwargs):
        if refresh:
            return await self.__handle_in_session(call_next, refresh=True, *args, **kwargs)
        if update:
            return await self.__handle_in_session(call_next, refresh=False, *args, **kwargs)
        result = await self.__handle_in_session(call_next, *args, **kwargs)
        if fetch_one:
            return result.scalars().first()

        return result.scalars().all()

    @abstractmethod
    async def before_add(self, instance: Type[T] = None, *args, **kwargs):
        pass

    async def add(self, *args, **kwargs):
        async def _add(*in_args, **in_kwargs):
            instance = self.model(**in_kwargs)
            await self.before_add(instance, *in_args, **in_kwargs)
            self.session.add(instance)
            return instance

        return await self._exec(_add, fetch_one=False, refresh=True, *args, **kwargs)

    async def get_all(self, offset: int = 0, limit: int = 10):
        async def _get_all(in_offset, in_limit):
            query = select(self.model).offset(offset=in_offset).limit(limit=in_limit)
            return await self.session.execute(query)

        return await self._exec(_get_all, in_offset=offset, in_limit=limit, refresh=False, fetch_one=False)

    async def get_count(self):
        async def _get_count():
            query = select(func.count()).select_from(self.model)
            return await self.session.execute(query)

        return await self._exec(_get_count, refresh=False, fetch_one=False)

    async def get_by_id(self, id: UUID):
        async def _get_by_id(in_id: UUID):
            query = select(self.model).where(self.model.id == in_id)
            return await self.session.execute(query)

        user = await self._exec(_get_by_id, refresh=False, fetch_one=True, in_id=id)
        if user:
            return user
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    async def update(self, id: UUID, *args, **kwargs):
        async def _update(in_id: UUID, *in_args, **in_kwargs):
            instance = await self.get_by_id(id=in_id)
            for key, value in in_kwargs.items():
                logger.info(f"This is the value I got {value}")
                logger.info(f"This is the key {key}")
                setattr(instance, key, value)
            return instance

        await self._exec(_update, update=True, in_id=id, *args, **kwargs)
        after_commit = await self.get_by_id(id=id)
        return after_commit

    async def h_delete(self, id):
        async def _h_delete(in_id):
            instance = await self.get_by_id(id=in_id)
            return await self.session.delete(instance)

        return await self._exec(_h_delete, in_id=id, update=True)
