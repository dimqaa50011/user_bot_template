from environs import Env
from telethon import TelegramClient
from .config import CoreBot, DbConfig, Misk
from sqlalchemy.orm import declarative_base


class Loader:
    __env = Env()
    __env.read_env()
    
    __phone=__env.int("TG_PHONE")
    
    __tg_pass=__env.str("TG_PASS")

    __bot_conf = CoreBot(
        api_id=__env.int("API_ID"),
        api_hash=__env.str("API_HASH")
    )

    __db_conf = DbConfig(
        user=__env.str("DB_USER"),
        password=__env.str("DB_PASS"),
        database=__env.str("DB_NAME"),
        host=__env.str("DB_HOST")
    )

    __misk = Misk()

    DB_URL = f"postgresql+asyncpg://{__db_conf.user}:{__db_conf.password}@{__db_conf.host}/{__db_conf.database}"
    
    Base = declarative_base()

    __user_bot = TelegramClient(
        "my_app", api_id=__bot_conf.api_id, api_hash=__bot_conf.api_hash)
    
    @classmethod
    def load_phone_and_tg_password(cls):
        return (cls.__phone, cls.__tg_pass)

    @classmethod
    def load_user_bot(cls):
        return cls.__user_bot
    
    @classmethod
    def load_misk(cls):
        return cls.__misk

    
