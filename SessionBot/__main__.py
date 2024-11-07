import asyncio
import importlib
from pyrogram import idle
from SessionBot import LOGGER_ID, xemishra
from SessionBot.Plugins import ALL_MODULES

async def install():
    try:
        await xemishra.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)
    for all_module in ALL_MODULES:
        importlib.import_module("SessionBot.Plugins." + all_module)

    LOGGER.info(f"@{xemishra.username} Started.")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(install())
    LOGGER.info("Stopping String Gen Bot...")
