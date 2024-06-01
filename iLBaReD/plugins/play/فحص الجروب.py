import os
import time
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from strings.filters import command
from iLBaReD import app
import requests
from pyrogram import enums
import aiohttp
import datetime
from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from iLBaReD.core.call import Omar
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait


@app.on_message(filters.new_chat_members)
async def welcome(client: Client, message: Message):
    photo = await app.download_media(message.chat.photo.big_file_id)
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    chat_id = message.chat.id
    egypt_tz = timezone('Egypt')
    current_time = datetime.datetime.now(egypt_tz).strftime("%H:%M:%S")    
    date = message.date.strftime("%Y-%m-%d")
    await message.reply_photo(photo=photo, caption=f"لا تُسِئ اللفظ وإن ضَاق عليك الرَّد ♥️"\nنورت جروبنا ي رايق ♥️"\n\n-᚜ - اسمك » ⦗ {message.from_user.mention} ⦘ 😋♥️ ،\n-᚜ - يوزر نيم » ⦗ @{message.from_user.username} ⦘ 😋♥️ ،\n-᚜ - تاريخ الدخول » ⦗ {date} ⦘ 😋♥️ ،\n-᚜ - وقت الدخول » ⦗ {current_time} ⦘ 😋♥️ ،")
