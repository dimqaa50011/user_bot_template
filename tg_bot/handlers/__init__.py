from telethon import TelegramClient
from .base import register_base_handler


async def register_all_handlers(client: TelegramClient):
    await register_base_handler(client)