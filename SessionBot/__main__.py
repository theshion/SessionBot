import asyncio
import importlib
from pyrogram import idle
from SessionBot import LOGGER_ID, xemishra
from SessionBot.Plugins import ALL_MODULES

async def install():
    try:
        await xemishra.start()
    except Exception as ex:
        print(ex)
        quit(1)
    for all_module in ALL_MODULES:
        importlib.import_module("SessionBot.Plugins." + all_module)

    print(f"Successfully Started Your Session Bot !!")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(install())
    print("Stopping Session Bot... Bye Bye...")
