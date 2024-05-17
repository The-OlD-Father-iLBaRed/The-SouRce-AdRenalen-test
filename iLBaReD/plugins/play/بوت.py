import asyncio
import random
from pyrogram import enums, filters, Client
from pyrogram.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup)
from iLBaReD import app
from iLBaReD.misc import SUDOERS
from config import *

# قائمة رسائل الرد
Replay_Bot_Meseege = [
    "اسمي {name} يصحبي 💘 ⋅",
    "يسطا قولتلك اسمي {name} ☺️",
    "اي يزميلي 😂♥️ ،",
    "قلب البوت 🥹💘 ⋅",
    "ثانية بشقط التنية 😂💘 ،",
    "يعم والله بحبك بس ناديلي ب {name} 🙂",
    "اي ي معلم مين مزعلك",
    "ايوا جاااي 😂♥️ ،",
    "تبا لك ماذا تريد من امي 🙂"
]

# الاسم الافتراضي
name = "هههههه"

# دالة لتعيين اسم البوت
@app.on_message(filters.regex("تعيين اسم البوت") & filters.private & SUDOERS, group=7113)
async def set_name_Bot(client, message):
    global name
    response = await app.ask(message.chat.id, "ارسل الاسم الجديد", filters=filters.text, timeout=30)
    name = response.text
    await message.reply_text("تم تعيين الاسم بنجاح")

# دالة للرد على الأوامر الخاصة بالبوت
@app.on_message(filters.command(["بوت", "البوت"], "") & filters.private, group=71135)
async def Bot_Nem_AdRenalen(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(Replay_Bot_Meseege).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])
    await message.reply_text(
        text=f"{bar}",
        disable_web_page_preview=True,
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.MARKDOWN
    )

# داله للدمج و المركدون
