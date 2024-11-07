from SessionBot.Plugins.inline import key
from Database.users import add_user
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from SessionBot import xemishra

@xemishra.on_message(filters.command("help"))
async def help(client, message):
  user_mention = message.from_user.mention
  text = f""" 
𝖧𝖾𝗒 {user_mention} 🇮🇳

**• 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌**

~ /about : 𝖳𝗈 𝖦𝖾𝗍 𝖨𝗇𝖿𝗈 𝖠𝖻𝗈𝗎𝗍 𝖳𝗁𝖾 𝖡𝗈𝗍.
~ /help : 𝖳𝗈 𝖦𝖾𝗍 𝖧𝖾𝗅𝗉 𝖬𝖾𝗇𝗎 𝖮𝖿 𝖳𝗁𝖾 𝖡𝗈𝗍.
~ /start : 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗍𝖺𝗋𝗍𝖾𝖽 𝖳𝗁𝖾 𝖡𝗈𝗍.
~ /generate : 𝖳𝗈 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝖲𝗍𝗋𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇.
~ /cancel : 𝖳𝗈 𝖢𝖺𝗇𝖼𝖾𝗅 𝖳𝗁𝖾 𝖮𝗇𝗀𝗈𝗂𝗇𝗀 𝖯𝗋𝗈𝖼𝖾𝗌𝗌.
~ /restart : 𝖳𝗈 𝖱𝖾𝗌𝗍𝖺𝗋𝗍 𝖳𝗁𝖾 𝖮𝗇𝗀𝗈𝗂𝗇𝗀 𝖯𝗋𝗈𝖼𝖾𝗌𝗌.
"""
  await message.reply_text(
        text=text,
        reply_markup=key,
        disable_web_page_preview=True,
    )
  await add_user(message.from_user.id)
