import time
import config
import logging
from pyrogram import Client
from datetime import datetime

# logging 
logging.basicConfig(level=logging.INFO, encoding="utf-8", format="%(asctime)s - %(levelname)s - \033[32m%(pathname)s: \033[31m\033[1m%(message)s \033[0m")

# creating pyrogram client 
xemishra = Client(
  "SessionBot",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  bot_token=config.BOT_TOKEN,
  in_memory=True,
  plugins=dict(root="SessionBot/Plugins"),
)

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
