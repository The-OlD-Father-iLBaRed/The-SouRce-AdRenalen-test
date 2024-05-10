import asyncio
import random
from pyrogram import enums
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import app
from iLBaReD.misc import SUDOERS
from iLBaReD.utils.database import get_served_chats

START_IMG_URL = "https://telegra.ph/file/0677e881a84925cb9c789.jpg"

MESSAGE = f"• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n\n- اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه 😋♥️ ،\n\n- بدون تهنيج او تقطيع او توقف مع مميزات رائعة 😋♥️ ،\n\n- كل ما عليك رفع البوت ادمن في قناتك او مجموعتك 😋♥️ ،\n\n- واستمتع بجوده الصوت و السرعه الخياليه للبوت 😋♥️ ،[• ⌯ 𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝐎𝐌𝐀𝐑 ⌯ •](https://t.me/DEV_ADRENALEN)\n[• ⌯ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋.𝐒𝐎𝐔𝐑𝐂𝐄 ⌯ •](https://t.me/WA_AdRenalen)\n[• ⌯ 𝐒𝐔𝐏𝐏𝐔𝐑𝐓.𝐒𝐎𝐔𝐑𝐂𝐄 ⌯ •](https://t.me/BaR_AdRenalen)\n[• ⌯ 𝐁𝐎𝐓 ⌯ •](https://t.me/{app.username})"

@app.on_message(filters.command(["ترويج"], "") & SUDOERS)
async def almortagel_bot(client, message):
    await send_message_to_chats()

async def send_message_to_chats():
    try:
        chats = await get_served_chats()
        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):
                try:
                    async for photo in client.get_chat_photos("me", limit=1):
                    await message.reply_photo(photo.file_id, caption=MESSAGE, reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "• ⌯ اضف البوت الي مجموعتك او قناتك ⌯ •", url=f"https://t.me/{app.username}?startgroup=true"),
            ]
        ]
         ),parse_mode=enums.ParseMode.MARKDOWN)
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Failed to send message to chat {chat_id}: {e}")
    except Exception as e:
        print(f"Error while fetching chats: {e}")
