import os
from dotenv import load_dotenv

# To load all env vars
load_dotenv()

#Apis 
API_ID = int(os.getenv("API_ID", "")) # get it from my.telegram.org and fill here.
API_HASH = os.getenv("API_HASH", "") # get it from my.telegram.org and fill here.

#Tokens
BOT_TOKEN = os.getenv("BOT_TOKEN", "") # get it from @BotFather on telegram by creating a new bot and fill here that bot token.

#Database
MONGODB_URI = os.getenv("MONGODB_URI", "") # get it from mongodb.com and fill here.

#Owner
LOGGER_ID = int(os.getenv("LOGGER_ID", "")) # get it by creating a logs group on telegram.
OWNER_ID int(os.getenv("OWNER_ID", "")) # flll here your bot owner telegram account id.

#Extra 
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/xemishra") # fill here your bot support group link 
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "https://t.me/xemishra") # fill here your updates channel link here 
