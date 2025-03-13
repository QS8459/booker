from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine
from src.conf.settings import settings


engine: AsyncEngine = create_async_engine(f"{settings.db_url}")

async_engine = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False

)
