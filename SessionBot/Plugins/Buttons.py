from pyrogram.types import InlineKeyboardButton

generate_single_button = [InlineKeyboardButton("𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝖲𝖾𝗌𝗌𝗂𝗈𝗇", callback_data="generate")]

buttons = [
        generate_single_button,
        [InlineKeyboardButton("𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url="https://t.me/xemishra")],
        [
            InlineKeyboardButton("𝖧𝖾𝗅𝗉", callback_data="help"),
            InlineKeyboardButton("𝖠𝖻𝗈𝗎𝗍", callback_data="about")
        ],
        [InlineKeyboardButton("𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url="https://t.me/xemishra")],
]
