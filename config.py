import os
from dotenv import load_dotenv

# To load all env vars
load_dotenv()

#Apis 
API_ID = int(os.getenv("API_ID", "28102624")) # get it from my.telegram.org and fill here.
API_HASH = os.getenv("API_HASH", "4e03913f9a576278ed4dbcdf7073e1b0") # get it from my.telegram.org and fill here.

#Tokens
BOT_TOKEN = os.getenv("BOT_TOKEN", "7737621490:AAHnAjyvw1mxzsviGGCVuiCIPdx4gqR9nd0") # get it from @BotFather on telegram by creating a new bot and fill here that bot token.

#Database
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://xemishra:3z8blpvVeMcKoZHs@truecallerxebot.46tc2.mongodb.net/?retryWrites=true&w=majority&appName=TrueCallerXeBot") # get it from mongodb.com and fill here.

#Owner
LOGGER_ID = int(os.getenv("LOGGER_ID", "7644065212")) # get it by creating a logs group on telegram.
OWNER_ID = int(os.getenv("OWNER_ID", "7644065212")) # flll here your bot owner telegram account id.

#Extra 
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/xemishra") # fill here your bot support group link 
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "https://t.me/xemishra") # fill here your updates channel link here 
