import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import app
from iLBaReD.misc import SUDOERS
from iLBaReD.utils.database import get_served_chats

START_IMG_URL = "https://telegra.ph/file/0677e881a84925cb9c789.jpg"

MESSAGE = f"• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n\n- اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه😋♥️ ،\n\n- بدون تهنيج او تقطيع او توقف مع مميزات رائعة 😋♥️ ،\n\n- كل ما عليك رفع البوت ادمن فقناتك او مجموعتك واستمتع 😋♥️ ،\n[⌯𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝐎𝐌𝐀𝐑⌯](https://t.me/DEV_ADRENALEN)\n[⌯𝐂𝐇𝐀𝐍𝐍𝐄𝐋.𝐒𝐎𝐔𝐑𝐂𝐄⌯](https://t.me/WA_AdRenalen)\n[⌯𝐒𝐔𝐏𝐏𝐔𝐑𝐓.𝐒𝐎𝐔𝐑𝐂𝐄⌯](https://t.me/BaR_AdRenalen)\n[⌯𝐁𝐎𝐓⌯](https://t.me/{app.username})"
BUTTON = InlineKeyboardMarkup([
    [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{app.username}?startgroup=True")]
])

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
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Failed to send message to chat {chat_id}: {e}")
    except Exception as e:
        print(f"Error while fetching chats: {e}")
