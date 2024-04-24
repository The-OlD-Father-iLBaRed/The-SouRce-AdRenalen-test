#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅
import asyncio
from asyncio import gather
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import time
import requests
from pyrogram import enums
from pyrogram import types
import aiohttp
from pyrogram.types import CallbackQuery
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from iLBaReD import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from iLBaReD import app
from iLBaReD import config
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait

OWNER_ID = getenv("OWNER_ID")


stiklok = []
photos_lock = []
forward_lock = []
link_lock = []
mention_lock = []

@app.on_message(filters.command(["قفل الملصقات","تعطيل الملصقات"],""))
async def block_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مقفلة من قبل")
        stiklok.append(message.chat.id)
        return await message.reply_text(f"تم قفل الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.command(["فتح الملصقات","تفعيل الملصقات"],""))
async def unblock_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in stiklok:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مفتوحة من قبل")
        stiklok.remove(message.chat.id)
        return await message.reply_text(f"تم فتح الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.sticker)
async def delete_stickers(client:Client, message:Message):
    if message.chat.id in stiklok:
        await message.delete()
        await message.reply(f"لا يمكنك ارسال الملصقات هنا 😋♥️ ،[{message.from_user.first_name}](tg://user?id={message.from_user.id}"f")",
        reply_to_message_id=m.message_id,
        parse_mode="Markdown")
        return


@app.on_message(filters.command(["عمر","مطور السورس","مطور","المطور","ادرنالين","ادرينالين"], ""), group=666)
async def kas(client: Client, message: Message):
    usr = await client.get_chat(OWNER_ID)
    name = usr.first_name
    bio = usrr.bio
    id = usrr.id
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       
    caption=f"-᚜ - الاسم » ⦗ {name} ⦘ 💘 ⋅\n-᚜ - اليوزر » ⦗ @{usr.username} ⦘ 💘 ⋅\n-᚜ - الايدي » ⦗ {usr.id} ⦘ 💘 ⋅\n-᚜ - البايو » ⦗ {usr.bio} ⦘ 💘 ⋅", 
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
    
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name
    await app.send_message(OWNER_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
    return await app.send_message(config.OWNER_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
