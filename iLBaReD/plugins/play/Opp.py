import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from random import choice
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from iLBaReD import app
from typing import Union
from pyrogram.types import InlineKeyboardButton


stayle_pic = []
The_Stayle_Pic = ["صورتك رايقة يصحبي","صورتك حلوة شوية","اي وشك دا يقطع الخميرة من البيت","تلاق تلاتة اتخديت من مالك","صورتك دي ولا القمر","عايز اتصور صورة معاك","انتا فجمال جورجينا","متحولش تغريني بغمزاتك","صورتك تشبه القمر"]


@app.on_message(filters.command(["تعطيل صورتي", "قفل صورتي"], "") & filters.group)
async def iddlock(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in stayle_pic:
            return await message.reply_text("صورتي معطل من قبل  😋♥️ ،")
        stayle_pic.append(message.chat.id)
        return await message.reply_text("تم تعطيل صورتي بنجاح 😋♥️ ،")
    else:
        return await message.reply_text("عذرا عزيزي هذا الامر للمشرفين بس 😋♥️ ،")

@app.on_message(filters.command(["فتح صورتي", "تفعيل صورتي"], "") & filters.group)
async def iddopen(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in stayle_pic:
            return await message.reply_text("صورتي مفعل من قبل 😋♥️ ،")
        stayle_pic.remove(message.chat.id)
        return await message.reply_text("تم تعطيل صورتي بنجاح 😋♥️ ،")
    else:
        return await message.reply_text("عذرا عزيزي هذا الامر للمشرفين بس 😋♥️ ،")

@app.on_message(filters.command(["ايدي"], ""))
async def muid(client: Client, message):
    if message.chat.id in stayle_pic:
        return await message.reply_text("صورتي معطل اطلب من المشرفين تفتحه 😋♥️ ،")
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.get_chat_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""{choice(The_Stayle_Pic)}  😋♥️ ،""", 
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
    



    
