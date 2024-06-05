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
import os
import requests
import aiohttp
import aiofiles
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import app


@app.on_message(filters.command(["تيك"], ""))
async def tiktok_video(client, message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("اعمل ريبلاي علي الرابط 😋♥️ ،")
    if not reply.link:
    try:
        text = await message.reply("- جاري التحميل من التيك توك بدون علامة مائيه واعلا جوده 😋♥️ ،")
        async def progress(current, total):
            await text.edit_text(f"يتم تحميل الفديو ↬ ⦗ {current * 100 / total:.1f}% ⦘ 😋♥️ ،")
    query = " ".join(message.command[1:])
    idd = message.from_user.id
    mc = message.chat.id
    url = "https://www.tikwm.com/api/?url={}".format(query)
    res = requests.get(url).json()
    video = res['data']['play']
    title = res['data']['title']
    share = InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ›", url=f"https://t.me/WA_AdRenalen"), 
                    InlineKeyboardButton(
                        "‹ 𝐒𝐔𝐏𝐏𝐔𝐑𝐓 ›", url=f"https://t.me/BAR_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "• ⌯ اضف البوت الي مجموعتك او قناتك ♥️ ⌯ •", url=f"https://t.me/{app.username}?startgroup=true"),
            ]
        ]
         ),     
    await message.reply_video(
        video=video,
        caption='• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n#عمر_ادرينالين {}'.format(title),
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ›", url=f"https://t.me/WA_AdRenalen"), 
                    InlineKeyboardButton(
                        "‹ 𝐒𝐔𝐏𝐏𝐔𝐑𝐓 ›", url=f"https://t.me/BAR_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "- مشاركة الفديو 😋♥️ ،", url='https://t.me/share/url?url={}'.format(query)),
            ]
        ]
         ),)


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
        egypt_tz = timezone( Egypt )
        current_time = datetime.datetime.now(egypt_tz).strftime("%H:%M:%S")    
        date = message.date.strftime("%Y-%m-%d")
        bot_username = (await app.get_me()).username
        await app.send_photo(
            chatid, 
            photo=photo, 
            caption=f"لا تُسِئ اللفظ وإن ضَاق عليك الرَّد ♥️ -\nنورت جروبنا ي رايق ♥️ -\n\n-᚜ - اسمك » ⦗ {message.from_user.mention} ⦘ 😋♥️ ،\n-᚜ - يوزر نيم » ⦗ @{message.from_user.username} ⦘ 😋♥️ ،\n-᚜ - تاريخ الدخول » ⦗ {date} ⦘ 😋♥️ ،\n-᚜ - وقت الدخول » ⦗ {current_time} ⦘ 😋♥️ ،",     
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
                [InlineKeyboardButton("خدني  لجروبك والنبي🥺♥", url=f"https://t.me/{app.username}?startgroup=True")]
            ]))
