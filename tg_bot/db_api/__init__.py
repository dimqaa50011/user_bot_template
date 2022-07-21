from .models import Users
from tg_bot.core import Loader
from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection


async def create_tables():
    Base = Loader.Base
    engine = create_async_engine(Loader.DB_URL)

    async with engine.begin() as connection:
        connection: AsyncConnection

        await connection.run_sync(Base.metadata.create_all)
