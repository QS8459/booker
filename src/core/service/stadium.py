from typing import Type

from fastapi import Depends

from src.core.utils.distance import calculate_distance
from src.core.base import BaseService, T
from src.db.models.stadium import Stadium
from src.db.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


class StadiumService(BaseService):

    def __init__(self, session: AsyncSession):
        super().__init__(session, Stadium)

    async def before_add(self, instance: Type[T] = None, *args, **kwargs):
        pass

    async def get_by_distance(
            self,
            u_lat: float,
            u_long: float,
            page: int = 1,
            page_size:int = 10
    ):
        stadiums = await self.get_all()
        distances_list: list = []
        for stadium in stadiums:
            distance = calculate_distance(u_lat, stadium.lat, u_long, stadium.long)
            setattr(stadium, 'distance', distance)
            distances_list.append(stadium)
        sorted_distances_list = sorted(distances_list, key=lambda stadium_: stadium.distance)

        start = (page - 1) * page_size
        end = start + page_size
        paginated_distances_list = sorted_distances_list[start:end]

        return paginated_distances_list


def get_stadium_service(session: AsyncSession = Depends(get_async_session)):
    return StadiumService(session)
