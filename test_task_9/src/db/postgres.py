from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.config.config import settings

Base = declarative_base()


engine = create_async_engine(
    settings.postgres.get_uri
)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session():
    """Генерирует асинхронные сессии."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
