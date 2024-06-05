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
import subprocess
try:
    from TikTok import TikTok_dl as TK
except ImportError:
    os.system('pip install TikTok-dl')
try:
    import requests
except ImportError:
    os.system('pip install requests')


@app.on_message(filters.command(["تيك"], ""))
async def tiktok_video(client, message):
    if message.text:
        try:
            global text,chatid,messageid,vd_status,wm_status,ad_status

            if re.search(r'https://vm.tiktok.com/(.*?)/?k=1',message.text) or re.search(r'',message.text):
                text = message.text

                chatid = message.chat.id

                messageid = message.message_id

                vd_status = 'تحميل باعلئ دقه'

                wm_status = 'تحميل بعلامه مائيه'

                ad_status = 'تحميل كملف صوتي'

                img = io.BytesIO(requests.get(TK(message.text).image).content)

                keyboar = [
                    [types.InlineKeyboardButton(vd_status,callback_data='vd'),types.InlineKeyboardButton(wm_status,callback_data='wm')],
                    [types.InlineKeyboardButton(ad_status,callback_data='ad')]
                ]

                mark = types.InlineKeyboardMarkup(keyboard=keyboar)
                
                bot.send_photo(chatid,img,reply_markup=mark)
        except:pass
@app.callback_query_handler(func=(lambda call:True))
def call(call):
    global ad_status,vd_status,wm_status
    if call.data == 'vd':
        try:

            bot.send_video(chatid,TK(text).nowatermark)
            
            vd_status = "تم التحميل"

            keyboar = [
                [types.InlineKeyboardButton(vd_status,callback_data='vd'),types.InlineKeyboardButton(wm_status,callback_data='wm')],
                
                [types.InlineKeyboardButton(ad_status,callback_data='ad')]
            ]
            
            mark = types.InlineKeyboardMarkup(keyboard=keyboar)

            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=mark)
        except:pass
    if call.data == 'ad':
        try:
            bot.send_audio(chatid,TK(text).audio)

            ad_status = "تم التحميل"

            keyboar = [
                [types.InlineKeyboardButton(vd_status,callback_data='vd'),types.InlineKeyboardButton(wm_status,callback_data='wm')],
                
                [types.InlineKeyboardButton(ad_status,callback_data='ad')]
            ]

            mark = types.InlineKeyboardMarkup(keyboard=keyboar)

            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=mark)
        except:pass
    if call.data == 'wm':
        try:
            bot.send_video(chatid,TK(text).watermark)

            wm_status = "تم التحميل"

            keyboar = [
                [types.InlineKeyboardButton(vd_status,callback_data='vd'),types.InlineKeyboardButton(wm_status,callback_data='wm')],
                
                [types.InlineKeyboardButton(ad_status,callback_data='ad')]
            ]

            mark = types.InlineKeyboardMarkup(keyboard=keyboar)

            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=mark)
        except:pass

#حقوقي شرفك تغير تثبت مدئ فشلك
#My rights, your honor has changed, to prove the extent of your failure 
bot.infinity_polling()
 




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
