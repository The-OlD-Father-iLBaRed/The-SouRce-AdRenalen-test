import asyncio
import random
from pyrogram import enums
from pyrogram import types
from iLBaReD.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from iLBaReD import app
from config import *
import speech_recognition as sr
from pyrogram import Client, filters
from pydub import AudioSegment
from os import remove

@@app.on_message(filters.regex("اكتب")& filters.group)
async def speech_to_text(client, message):
    if not message.reply_to_message:
        await message.reply("الرد على صوت.")
        return
    await message.reply("جاري تحميل الصوت")
    voice_down = await message.reply_to_message.download("./recyad.wav")
    voice = sr.Recognizer()
    await message.reply("جاري استخراج سورس الصوت")
    sound = AudioSegment.from_ogg(voice_down)
    wav_file = sound.export(voice_down, format="wav")
    with sr.AudioFile(wav_file) as source:
        audio_source = voice.record(source)
    await message.reply("جاري التعرف علي الكلام")
    try:
        text = voice.recognize_google(audio_source, language= ar-EG )
    except Exception as e:
        text = f"فشل التعرف علي الكلام\n{e}"
    await message.reply(text)
    remove("recyad.wav")
async def is_heroku():
    return "heroku" in socket.getfqdn()



AdRenalen_Bot={}

The_Name_Bot = ["اسمي {name} يصحبي 💘 ⋅","يسطا قولتلك اسمي {name } ☺️","اي يزميلي 😂♥️ ،","قلب البوت 🥹💘 ⋅","ثانية بشقط التنية 😂💘 ،","يعم والله بحبك بس ناديلي ب {name} 🙂","اي ي معلم مين مزعلك","ايوا جاااي 😂♥️ ،","تبا لك ماذا تريد من امي 🙂",]

name = "ادرينالين"

@app.on_message(filters.regex("تعيين اسم البوت")& filters.private & SUDOERS, group=7113)
async def AdRenalen_Bot(client, message):
    global name
    neme = await app.neme(message.chat.id, "ارسل الاسم الجديد")
    name = neme.text
    await message.reply_text("تم تعيين الاسم بنجاح")


@app.on_message(filters.command(["بوت", "البوت"], ""), group=71135)
async def AdRenalen_Bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(The_Name_Bot).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])
    
    await message.reply_text(
        text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
        disable_web_page_preview=True,
        reply_markup=keyboard,
    parse_mode=enums.ParseMode.MARKDOWN)

