import asyncio
from pyrogram.types import Message
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from random import choice
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from iLBaReD import app
from typing import Union
from pyrogram.types import InlineKeyboardButton

Gmale_pic = []

@app.on_message(filters.command(["تعطيل جمالي", "قفل جمالي"], "") & filters.group)
async def iddlock(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in Gmale_pic:
            return await message.reply_text("امر جمالي معطل من قبل  😋♥️ ،")
        Gmale_pic.append(message.chat.id)
        return await message.reply_text("تم تعطيل امر جمالي بنجاح 😋♥️ ،")
    else:
        return await message.reply_text("عذرا عزيزي هذا الامر للمشرفين بس 😋♥️ ،")

@app.on_message(filters.command(["فتح جمالي", "تفعيل جمالي"], "") & filters.group)
async def iddopen(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in Gmale_pic:
            return await message.reply_text("امر جمالي مفعل من قبل 😋♥️ ،")
        Gmale_pic.remove(message.chat.id)
        return await message.reply_text("تم تعطيل امر جمالي بنجاح 😋♥️ ،")
    else:
        return await message.reply_text("عذرا عزيزي هذا الامر للمشرفين بس 😋♥️ ،")

@app.on_message(filters.command(["جمالي","ص"], ""))
async def muid(client: Client, message):
    if message.chat.id in Gmale_pic:
        return await message.reply_text("جمالي معطل اطلب من المشرفين تفتحه 😋♥️ ،")
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    Omar = random.randint(1, 1000)
    async for photo in client.get_chat_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""- نسبة جمالك هيا » ⦗  {Omar} ⦘😋♥️ ،""", 
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ›", url=f"https://t.me/WA_AdRenalen")
                ]
            ]
        ),
    )
    



    