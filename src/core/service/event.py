from typing import Type
from fastapi import Depends
from src.db.models.event import Event
from src.core.base import BaseService, T
from src.db.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


class EventService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Event)

    async def before_add(self, instance: Type[T] = None, *args, **kwargs):
        pass


def get_event_service(session: AsyncSession = Depends(get_async_session)):
    return EventService(session)
