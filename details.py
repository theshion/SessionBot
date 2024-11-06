from pyrogram.types import InlineKeyboardButton

class Data:
    generate_single_button = [InlineKeyboardButton("Start Generating Session", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Home", callback_data="home")]
    ]
    generate_button = [generate_single_button]
    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Support ", url="https://t.me/xemishra")],
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [InlineKeyboardButton("Updates", url="https://t.me/xemishra")],
    ]
