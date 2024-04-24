import asyncio
from asyncio import gather
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import time
import aiohttp
from pyrogram.types import CallbackQuery
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from iLBaReD import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from iLBaReD import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait


iddof = []
id = {}

@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "") & filters.group)
async def iddlock(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in iddof:
            return await message.reply_text("الايدي معطل من قبل  😋♥️ ،")
        iddof.append(message.chat.id)
        return await message.reply_text("تم تعطيل الايدي بنجاح 😋♥️ ،")
    else:
        return await message.reply_text("عذرا عزيزي هذا الامر للمشرفين بس 😋♥️ ،")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "") & filters.group)
async def iddopen(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in iddof:
            return await message.reply_text("الايدي مفعل من قبل 😋♥️ ،")
        iddof.remove(message.chat.id)
        return await message.reply_text("تم تعطيل الايدي بنجاح 😋♥️ ،")
    else:
        return await message.reply_text("عذرا عزيزي هذا الامر للمشرفين بس 😋♥️ ،")

@app.on_message(filters.command(["ايدي"], ""))
async def muid(client: Client, message):
    if message.chat.id in iddof:
        return await message.reply_text("الايدي معطل اطلب من المشرفين تفتحه 😋♥️ ،")
    
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
    
    caption = f"𝅄 𓏺 𝐂𝐇𝐀𝐓 𝐍𝐄𝐌 » ⦗ {chat} ⦘ 🕷 ⋅\n𝅄 𓏺 𝐍𝐄𝐌 » ⦗ {user.first_name} ⦘ 🕷 ⋅\n𝅄 𓏺 𝐔𝐒𝐄𝐑 𝐍𝐄𝐌 » ⦗ [@{user.username}] ⦘ 🕷 ⋅\n𝅄 𓏺 𝐁𝐈𝐎 » ⦗ {bio} ⦘ 🕷 ⋅\n𝅄 𓏺 𝐈𝐃 » ⦗ {user.id} ⦘ 🕷 ⋅\n𝅄 𓏺 𝐂𝐇𝐀𝐓 𝐈𝐃 » ⦗ {chat_id} ⦘ 🕷 ⋅"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} ♥️", callback_data=f"heart{user_id}")]])
    
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
     await query.answer("قلبك علي قلبي مينفعش تشيلو 😂♥️ ،",show_alert=True)
    
    idd = len(id[user.id])
    
    caption = f"𝅄 𓏺 𝐂𝐇𝐀𝐓 𝐍𝐄𝐌 » ⦗ {query.chat.title} ⦘ 🕷 ⋅\n𝅄 𓏺 𝐍𝐄𝐌 » ⦗ {user.first_name} ⦘ 🕷 ⋅\n𝅄 𓏺 𝐔𝐒𝐄𝐑 𝐍𝐄𝐌 » ⦗ [@{user.username}] ⦘ 🕷 ⋅\n𝅄 𓏺 𝐁𝐈𝐎 » ⦗ {user.bio} ⦘ 🕷 ⋅\n𝅄 𓏺 𝐈𝐃 » ⦗ {user.id} ⦘ 🕷 ⋅\n𝅄 𓏺 𝐂𝐇𝐀𝐓 𝐈𝐃 » ⦗ {query.chat.id} ⦘ 🕷 ⋅"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} ♥️", callback_data=f"heart{user_id}")]])
    
    await query.edit_message_text(caption, reply_markup=reply_markup)
