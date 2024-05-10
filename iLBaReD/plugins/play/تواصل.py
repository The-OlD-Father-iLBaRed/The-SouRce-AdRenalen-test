import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from random import choice
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from iLBaReD import app
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram import Client, filters
from strings.filters import command
from iLBaReD import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

#############################

The_ConTacT_Dev = []

@app.on_message(filters.command(["تعطيل تواصل", "قفل تواصل"], "") & filters.group)
async def iddlock(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER]:
        if message.chat.id in The_ConTacT_Dev:
            return await message.reply_text("امر تواصل معطل من قبل  😋♥️ ،")
        The_ConTacT_Dev.append(message.chat.id)
        return await message.reply_text("تم تعطيل امر تواصل بنجاح 😋♥️ ،")
    else:
        return await message.reply_text("عذرا عزيزي هذا الامر للمشرفين بس 😋♥️ ،")

@app.on_message(filters.command(["فتح تواصل", "تفعيل تواصل"], "") & filters.group)
async def iddopen(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER]:
        if message.chat.id not in The_ConTacT_Dev:
            return await message.reply_text("امر تواصل مفعل من قبل 😋♥️ ،")
        The_ConTacT_Dev.remove(message.chat.id)
        return await message.reply_text("تم فتح امر تواصل بنجاح 😋♥️ ،")
    else:
        return await message.reply_text("عذرا عزيزي هذا الامر للمشرفين بس 😋♥️ ،")
        
@app.on_message(filters.text & (filters.channel | filters.private))            
async def muid(client: Client, message):
    if message.chat.id in The_ConTacT_Dev:
        return await message.reply_text("تواصل معطل اطلب من المشرفين تفتحه 😋♥️ ،")
    msg = message.text
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    usr_id = message.from_user.id
    mention = message.from_user.mention
    await app.send_message("OWNER_ID", f"⌯ قام {mention} \n\n⌯ بارسال رسالة للبوت \n\n- {msg}")
