import asyncio
import random
from pyrogram import enums
from pyrogram import types
from iLBaReD.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from iLBaReD import app
from config import *
from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from iLBaReD  import app 
mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')


@app.on_message(filters.command(["فحص المونجو","فحص"],""))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("- استخدم الامر مثل ⦗ فحص + mongodb ⦘")
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("- كود المنجو دا شغال تقدر تستخدمو ✨♥️ ،")
        except Exception as e:
            await message.reply(f"- فشل الاتصال السبب : {e}")
    else:
        await message.reply("- الكود دا مش شغال مينفعش تستخدمو ✨♥️ ،")

########################################
Replay_Bot_Meseege = ["اسمي {name} يصحبي 💘 ⋅","يسطا قولتلك اسمي {name } ☺️","اي يزميلي 😂♥️ ،","قلب البوت 🥹💘 ⋅","ثانية بشقط التنية 😂💘 ،","يعم والله بحبك بس ناديلي ب {name} 🙂","اي ي معلم مين مزعلك","ايوا جاااي 😂♥️ ،","تبا لك ماذا تريد من امي 🙂",]
########################################
name = ""
########################################
@app.on_message(filters.regex("تعيين اسم البوت")& filters.private & SUDOERS, group=7113)
async def set_name_Bot(client, message):
    global name
    neame = await app.ask(message.chat.id, "ارسل الاسم الجديد", filters=filters.text, timeout=30)
    name = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")
########################################
@app.on_message(filters.command(["بوت", "البوت"], ""), group=71135)
async def Bot_Nem_AdRenalen(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(Replay_Bot_Meseege).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=True")]])
    await message.reply_text(
        text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
        disable_web_page_preview=True,
        reply_markup=keyboard,
    parse_mode=enums.ParseMode.MARKDOWN)
