import asyncio
from pyrogram import Client, idle
from SessionBot import xemishra

async def install():
  await xemishra.start()
  x = await xemishra.get_me()
  print("Your SessionBot {x.first_name} Has Been Started Successfully!")
  await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(install())
