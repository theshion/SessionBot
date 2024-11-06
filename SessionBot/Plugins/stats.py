from pyrogram import Client as xemishra, filters
from SessionBot import OWNER_ID
from Database.users import get_users


    users = len(await get_users())
    await message.reply_text("")
