from SessionBot.Plugins.Buttons import buttons
from pyrogram import Client as xemishra, filters
from pyrogram.types import InlineKeyboardMarkup

@xemishra.on_message(filters.command("about"))
def about(client, message):
  chat_id = message.chat.id
  user_mention = message.from_user.mention
  text = f"""
𝖧𝖾𝗒 {user_mention} 🇮🇳

**𝖠𝖻𝗈𝗎𝗍 𝖳𝗁𝗂𝗌 𝖡𝗈𝗍** 

𝖳𝗁𝗂𝗌 𝖨𝗌 𝖠 𝖲𝗍𝗋𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗈𝗋 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖡𝗈𝗍 𝖳𝗈 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝖯𝗒𝗋𝗈 𝗏1 𝖺𝗇𝖽 𝖯𝗒𝗋𝗈 𝗏2 𝖺𝗇𝖽 𝖳𝖾𝗅𝖾𝗍𝗁𝗈𝗇 𝖲𝗍𝗋𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖡𝗒 @xemishra

**• 𝖲𝗈𝗎𝗋𝖼𝖾 𝖢𝗈𝖽𝖾 :** [Click Here](https://xemishra.t.me)

**• 𝖥𝗋𝖺𝗆𝖾𝗐𝗈𝗋𝗄 :** [Pyrogram](https://docs.pyrogram.org)

**• 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 :** [Python](https://www.python.org)

**• 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 :** @xemishra
  """
   await client.send_message(
        chat_id,
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
   )
