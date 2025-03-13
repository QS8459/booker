from typing import Type

from fastapi import Depends
from src.db.models.booking import Booking
from src.db.engine import get_async_session
from src.core.base import BaseService, T

from sqlalchemy.ext.asyncio import AsyncSession


class BookingService(BaseService):

    def __init__(self, session: AsyncSession):
        super().__init__(session, Booking)

    async def before_add(self, instance: Type[T] = None, *args, **kwargs):
        pass


def get_booking_service(session: AsyncSession = Depends(get_async_session)):
    return BookingService(session)
