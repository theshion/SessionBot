from SessionBot.Plugins.Buttons import buttons
from pyrogram import Client as xemishra, filters
from pyrogram.types import InlineKeyboardMarkup, Message

@xemishra.on_message(filters.command("start"))
def start(client, message):
  chat_id = message.chat.id
  user_mention = message.from_user.mention
  x = client.get_me()
  text = f"""
𝖧𝖾𝗒 {user_mention} 🇮🇳

𝖨'𝗆 𝖳𝗁𝖾 𝖬𝗈𝗌𝗍 𝖳𝗋𝗎𝗌𝗍𝖾𝖽 𝖠𝗇𝖽 𝖥𝖺𝗌𝗍𝖾𝗌𝗍 𝖲𝗍𝗋𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗈𝗋 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖡𝗈𝗍.\n\n🍀 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝖲𝗍𝗋𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇𝗌:

• 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖵1
• 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖵2
• 𝖳𝖾𝗅𝖾𝗍𝗁𝗈𝗇
• 𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆
  
𝖥𝗈𝗋 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝗌𝖾𝗌𝗌𝗂𝗈𝗇 𝖢𝗅𝗂𝖼𝗄 𝖮𝗇 "𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝖲𝖾𝗌𝗌𝗂𝗈𝗇" 𝖡𝗎𝗍𝗍𝗈𝗇 𝖡𝖾𝗅𝗈𝗐!
  """
   await client.send_message(
        chat_id,
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
   )
