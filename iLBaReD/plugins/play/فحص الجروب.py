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
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    chat_id = message.chat.id
    egypt_tz = timezone('Egypt')
    current_time = datetime.datetime.now(egypt_tz).strftime("%H:%M:%S")    
    date = message.date.strftime("%Y-%m-%d")
    await app.send_message(chat_id=chat_id, text=f"لا تُسِئ اللفظ وإن ضَاق عليك الرَّد\nɴᴀᴍᴇ ⌯ {message.from_user.mention}\nᴜѕᴇʀɴᴀᴍᴇ ⌯ @{message.from_user.username}\n𝖣𝖺𝗍𝖾 ⌯ {date}\n𝖳𝗂𝗆𝖾 ⌯ {current_time}")



@app.on_message(filters.command("وقت انضمامي"), group=701129011)
async def timeadd(app, message):
    user_joined = await app.get_chat_member(message.chat.id, message.from_user.id)
    current_time = user_joined.datetime.now(egypt_tz).strftime("%H:%M:%S")    
    date = user_joined.date.strftime("%Y-%m-%d")
    await app.send_message(chat_id=message.chat.id, text=f"وقت انضمامك إلى المجموعة: {date} {current_time}")



	
	
@app.on_message(filters.left_chat_member)
async def god_bay(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    chat_id = message.chat.id
    egypt_tz = timezone('Egypt')
    current_time = datetime.datetime.now(egypt_tz).strftime("%H:%M:%S")    
    date = message.date.strftime("%Y-%m-%d")
    await app.send_message(chat_id=chat_id, text=f"وَأَن لَّيْسَ لِلْإِنسَانِ إِلَّا مَا سَعَىٰ\nɴᴀᴍᴇ ⌯ {message.from_user.mention}\nᴜѕᴇʀɴᴀᴍᴇ ⌯ @{message.from_user.username}\n𝖣𝖺𝗍𝖾 ⌯ {date}\n𝖳𝗂𝗆𝖾 ⌯ {current_time}")




@app.on_message(~filters.private & command(["/gdata","فحص الجروب"]), group=2)
async def instatus(app, message):
    photo = await app.download_media(message.chat.photo.big_file_id)
    start_time = time.perf_counter()
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    count = await app.get_chat_members_count(message.chat.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,):
        deleted_acc = 0
        premium_acc = 0
        banned = 0
        bot = 0
        uncached = 0
        async for ban in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BANNED):
            banned += 1
        async for member in app.get_chat_members(message.chat.id):
            user = member.user
            if user.is_deleted:
                deleted_acc += 1
            elif user.is_bot:
                bot += 1
            elif user.is_premium:
                premium_acc += 1
            else:
                uncached += 1
        end_time = time.perf_counter()
        timelog = "{:.2f}".format(end_time - start_time)
        await message.reply_photo(photo=photo, caption=f"""
╭─《 • ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ • 》
├<b> -᚜ - اسم الـ جروب » ⦗ {message.chat.title} ⦘ 💘 ⋅</b>
├<b> -᚜ - عدد الـ اعضاء » ⦗ {count} ⦘ 💘 ⋅</b>
├<b> -᚜ - عدد الـ بوتات »  ⦗ {bot} ⦘ 💘 ⋅</b>
├<b> -᚜ - عدد الـ حسبات الـ محذوفه » ⦗ {deleted_acc} ⦘ 💘 ⋅</b>
├<b> -᚜ - عدد الـ مطرودين » ⦗ {banned} ⦘ 💘 ⋅</b>
├<b> -᚜ - عدد الاغنية الي موثقين هنا » ⦗ {premium_acc} ⦘ 😂💘 ⋅</b>
╰─《 • ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ • 》""")
    else:
        sent_message = await message.reply_text("يمكن للمسؤولين فقط!")
        await sleep(5)
        await sent_message.delete()


