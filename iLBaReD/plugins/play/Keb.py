import asyncio
from iLBaReD.plugins.play.xgame import callback_query
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings.filters import command
from iLBaReD import app
from config import OWNER_ID
from iLBaReD.misc import SUDOERS
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from iLBaReD import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from iLBaReD.misc import SUDOERS
import sys
from os import getenv

OWNER_ID = getenv("OWNER_ID")
OWNER_USER_NAME = getenv("OWNER_USER_NAME")
sniper = getenv(" sniper")

OWNER = getenv("OWNER")

from dotenv import load_dotenv
import re


@app.on_message(filters.command(["كيب", "✭ رجوع"]) & SUDOERS)

async def crsourceowner(client: Client, message: Message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


REPLY_MESSAGE = "**👋︙مـرحـبـا بـك عـزيـزي الـمـطـور ♥️**\n**✨︙فــي قـائـمـة التحـكـم بـالـبـوت💞**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("✭ WELCOME IN SOUCE  sniper ✭"),
    ],
    [
        ("✭ قسم الاذاعه"),
        ("✭ تحكم الحساب المساعد"),
    ],
    [
        
        ("✭ قسم الجروبات"),
        ("✭ قسم المطورين"),
       
    ],
    [
        ("✭ السورس"),
    ],
]



    
@app.on_message(filters.command(["✭ قسم الاذاعه"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ اذاعه عام","✭ اذاعه بالتوجيه"],["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)
    
@app.on_message(filters.command(["✭ السورس"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ قـنـاة الـسـورس","✭ للتواصل معنآ"], ["✭ مطور السورس"], ["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم السورس تحكم بالازار**", reply_markup=kep)
    
@app.on_message(filters.command(["✭ قسم المطورين"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ مـطـوريـنـك","✭ للتواصل معنآ"],  ["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم المطورين تحكم بالازار**", reply_markup=kep)

@app.on_message(filters.command(["✭ قسم الجروبات"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ الجروبات المحظوره","✭ الاحصائيات","✭ حـظـر الـجـروبـات"], ["✭ رجوع","✭ جـروبـاتـك النـشـطـه"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الجروبات تحكم بالازار**", reply_markup=kep)

