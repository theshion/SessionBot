import time
import config
import logging
import pyrogram
from datetime import datetime
from pyromod import Client
from pyrogram.enums import ParseMode

# logging 
logging.basicConfig(level=logging.INFO, encoding="utf-8", format="%(asctime)s - %(levelname)s - \033[32m%(pathname)s: \033[31m\033[1m%(message)s \033[0m")

# creating pyrogram client 
class xemishra(Client):
    def __init__(self):
        super().__init__(
            name="SessionBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            lang_code="en",
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention
    async def stop(self):
        await super().stop()


xemishra = xemishra()

# storing start time for ping command
StartTime = time.time()
START_TIME = datetime.now()

# defining All Vars
API_ID = config.API_ID
API_HASH = config.API_HASH
BOT_TOKEN = config.BOT_TOKEN
MONGODB_URI = config.MONGODB_URI
LOGGER_ID = config.LOGGER_ID
OWNER_ID = config.OWNER_ID
SUPPORT_CHAT = config.SUPPORT_CHAT
UPDATES_CHANNEL = config.UPDATES_CHANNEL
