from telethon import TelegramClient, events
from tg_bot.core import Loader


class BaseHandlers:
    client = Loader.load_user_bot()
    
    async def echo(self, event):
        msg = event.raw_text
        
        await self.client.send_message("me", msg)
        

async def register_base_handler(client: TelegramClient):
    base = BaseHandlers()
    
    client.add_event_handler(base.echo, events.NewMessage(chats=("me", )))
    