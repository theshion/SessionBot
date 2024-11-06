from pyrogram import Client as xemishra, filters
from pyrogram.types import InlineKeyboardMarkup, Message

@xemishra.on_message(filters.command("start"))
def start(client, message):
  user_mention = message.from_user.mention
  x = client.get_me()
  message = f"""
  Hey {user_mention} 

  i'm the trusted and most faster telegram bot using which you can generate all type of string session :

  • Pyrogram V1
  • Pyrogram V2
  • Telethon 
  • Instagram 

  for generating string session click on "Genrate session" Button Below
  """
