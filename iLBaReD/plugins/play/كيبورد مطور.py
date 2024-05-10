import asyncio
from SniperMusic.plugins.play.xgame import callback_query
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings.filters import command
from SniperMusic import app
from config import OWNER_ID
from SniperMusic.misc import SUDOERS
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from SniperMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from SniperMusic.misc import SUDOERS
import sys
from dotenv import load_dotenv
import re
from os import getenv
################################################
OWNER_ID = getenv("OWNER_ID")
OWNER_USER_NAME = getenv("OWNER_USER_NAME")
OWNER = getenv("OWNER")
################################################
@app.on_message(filters.command(["‹ الصفحة الرئيسية ›"]) & SUDOERS)
@app.on_message(filters.command(["/start"]) & SUDOERS)
async def crsourceowner(client: Client, message: Message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )

REPLY_MESSAGE = "- مرحبا بك عزيزي المطور 😋♥️ ،"
REPLY_MESSAGE_BUTTONS = [
[("‹ قسم الترويج ›"),("الاوامر")],
[("احرف"),("مطور السورس")],
[("تويت"),("صراحه")],
[("نكته"),("حكمه")],
[("انصحني"),("لو خيروك")],
[("‹ قسم الصور ›")],
[("‹ اغلاق الكيبورد ›")]]
################################################
@app.on_message(filters.command(["‹ قسم الترويج ›"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["‹ ترويج ›"],["‹ الصفحة الرئيسية ›"]], resize_keyboard=True)
    await message.reply_text("- مرحبا بك عزيزي المطور في قسم الترويج 😋♥️ ،", reply_markup=kep)
    