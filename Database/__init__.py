from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from config import MONGODB_URI

mongo = MongoCli(config.MONGODB_URI)
db = mongo.SessionBot
