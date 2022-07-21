import asyncio

from loguru import logger

from tg_bot.core import Loader
from tg_bot.db_api import create_tables
from tg_bot.handlers import register_all_handlers


async def runner():
    client = Loader.load_user_bot()

    phone, password = Loader.load_phone_and_tg_password()

    await create_tables()
    logger.info("Tables created")

    await register_all_handlers(client)
    logger.info("Handlers registered")

    await client.start(phone=phone, password=password)
    logger.info("Bot started")
    await client.run_until_disconnected()


if __name__ == "__main__":
    try:
        asyncio.run(runner())
    except (KeyboardInterrupt, SystemError):
        logger.warning("Bot stopped!!!")
