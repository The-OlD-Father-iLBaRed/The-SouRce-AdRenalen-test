import asyncio
import random
from pyrogram import enums, filters, Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
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
name = "ask"

# دالة لتعيين اسم البوت
@app.on_message(filters.regex("تعيين اسم البوت")& filters.private & SUDOERS, group=7113)
async def set_name_Bot(client, message):
    global name
    response = await client.ask(message.chat.id, "ارسل الاسم الجديد", filters=filters.text, timeout=30)
    name = response.text
    await message.reply_text("تم تعيين الاسم بنجاح")

# دالة للرد على الأوامر الخاصة بالبوت
@app.on_message(filters.command(["بوت", "البوت"]) & filters.private, group=71135)
async def Bot_Nem_AdRenalen(client, message):
    global name
    bot_username = (await client.get_me()).username
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


@Client.on_message(filters.command("تعين اسم البوت", ""))
async def set_bot(client: Client, message):
   NAME = await client.ask(message.chat.id,"♪ ارسل اسم البوت الجديد  💎 .", filters=filters.text, timeout=30)
   BOT_NAME = NAME.text
   bot_username = client.me.username
   await set_bot_name(bot_username, BOT_NAME)
   await message.reply_text("♪ تم تعين اسم البوت بنجاح  💎 .")


@Client.on_message(filters.command(["بوت", "البوت"], ""))
async def bottttt(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    bar = random.choice(selections).format(BOT_NAME)
    await message.reply_text(f"[{bar}](https://t.me/{bot_username}?startgroup=True)", disable_web_page_preview=True)
