from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SessionBot import SUPPORT_CHAT, UPDATES_CHANNEL

key = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝖲𝖾𝗌𝗌𝗂𝗈𝗇", callback_data="gensession")],
        [
            InlineKeyboardButton(text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url=UPDATES_CHANNEL
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖵1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖵2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="𝖳𝖾𝗅𝖾𝗍𝗁𝗈𝗇", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝖳𝗋𝗒 𝖠𝗀𝖺𝗂𝗇", callback_data="gensession")]]
)
