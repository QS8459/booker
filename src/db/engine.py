from src.conf.db_engine import async_engine
from sqlalchemy.ext.asyncio import AsyncSession


async def get_async_session() -> AsyncSession:
    async with async_engine() as session:
        yield session


