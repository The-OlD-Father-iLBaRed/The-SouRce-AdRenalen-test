import asyncio
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from iLBaReD import app
from iLBaReD.utils.database import is_on_off
from iLBaReD import app
import re
import sys
import os
import random
from time import time
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters






iddof = []
id = {}

@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "") & filters.group)
async def iddlock(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id in iddof:
            return await message.reply_text("♪ الامر معطل من قبل 💎 .")
        iddof.append(message.chat.id)
        return await message.reply_text("♪ تم تعطيل الايدي بنجاح 💎 .")
    else:
        return await message.reply_text("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط 💎 .")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "") & filters.group)
async def iddopen(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id not in iddof:
            return await message.reply_text("♪ الايدي مفعل من قبل 💎 .")
        iddof.remove(message.chat.id)
        return await message.reply_text("♪ تم تفعيل الايدي بنجاح 💎 .")
    else:
        return await message.reply_text("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط 💎 .")
        
    user = await client.get_chat(message.from_user.id)
    user_id = user.id
    username = user.username
    first_name = user.first_name
    bio = user.bio
    chat = message.chat.title
    chat_id = message.chat.id
   
    photo = user.photo.big_file_id
    if photo:
        photo = await client.download_media(photo)
    else:
        photo = None
    
    if user.id not in id:
        id[user.id] = []
    
    idd = len(id[user.id])
    
    caption = f"┇‌ ⤹•ɴᴀᴍᴇ : {user.first_name}\n┇‌ ⤹•ᴜsᴇʀ : @{username}\n┇‌ ═══════『♡』═══════\n┇‌ ⤹•ɪᴅ : {user_id}\n┇‌ ⤹•ʙɪᴏ : {bio}\n┇‌═══════『♡』═══════\n┇‌ ⤹•ᴄʜᴀᴛ : {chat}\n┇‌ ⤹•ᴄʜᴀᴛ ɪᴅ : {chat_id}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")]])
    
    await message.reply_photo(photo=photo, caption=caption, reply_markup=reply_markup)

@app.on_callback_query(filters.regex("heart"))
async def heart(client, query: CallbackQuery):
    callback_data = query.data.strip()
    callback_request = callback_data.replace("heart", "")
    user_id = int(callback_request)
    user = await client.get_chat(user_id)
    
    if user.id not in id:
        id[user.id] = []
    
    if query.from_user.mention not in id[user.id]:
        id[user.id].append(query.from_user.mention)
    else:
        id[user.id].remove(query.from_user.mention)
    
    idd = len(id[user.id])
    
    caption = f"┇‌ ⤹•ɴᴀᴍᴇ : {user.first_name}\n┇‌ ⤹•ᴜsᴇʀ : @{user.username}\n┇‌ ═══════『♡』═══════\n┇‌ ⤹•ɪᴅ : {user_id}\n┇‌ ⤹•ʙɪᴏ : {user.bio}\n┇‌═══════『♡』═══════\n┇‌ ⤹•ᴄʜᴀᴛ : {query.message.chat.title}\n┇‌ ⤹•ᴄʜᴀᴛ ɪᴅ : {query.message.chat.id}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")]])
    
    await query.edit_message_text(caption, reply_markup=reply_markup)
    