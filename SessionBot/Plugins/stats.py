from pyrogram import Client as xemishra, filters
from SessionBot import OWNER_ID
from Database.users import get_users

@xemishra.on_message(filters.command(["stats", "users"]) & filters.user(OWNER_ID))
async def stats(client, message):
    user_mention = message.from_user.mention
    users = len(await get_users())
    await message.reply_text(f"𝖧𝖾𝗒 {user_mention} 🇮🇳\n\n𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖲𝗍𝖺𝗍𝗌 𝖮𝖿 𝖳𝗁𝖾 𝖡𝗈𝗍 𝖨𝗌 :\n\n • {users} 𝖴𝗌𝖾𝗋𝗌")
