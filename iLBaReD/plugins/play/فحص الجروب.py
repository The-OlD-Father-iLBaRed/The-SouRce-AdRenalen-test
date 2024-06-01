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



@app.on_message(filters.new_chat_members, group=7130)
async def welcome(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
        m = await app.get_users(int(x[0]))
        chatid = message.chat.id
        photo = await client.download_media(message.chat.photo.big_file_id)
        bot_username = (await app.get_me()).username
        await app.send_photo(
            chatid, 
            photo=photo, 
            caption=f"- نورت ياا قمر 🌗😘🤝️ {message.from_user.mention}\n│ \n└ʙʏ في {message.chat.title}",     
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("مـالـك الـجـروب⚡", url=f"https://t.me/{m.username}")], 
                [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{app.username}?startgroup=True")]
            ]))

@app.on_message(filters.left_chat_member, group=7130)
async def goodbye(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
        m = await app.get_users(int(x[0]))
        chatid = message.chat.id
        photo = await client.download_media(message.chat.photo.big_file_id)
        bot_username = (await app.get_me()).username
        await app.send_photo(
            chatid, 
            photo=photo, 
            caption=f"- مشيت ليه يقلبي يلا بسلامات🥲👋\n│ \n└ʙʏ  {message.from_user.mention} ",     
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("مـالـك الـجـروب⚡", url=f"https://t.me/{m.username}")], 
                [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{app.username}?startgroup=True")]
            ]))
