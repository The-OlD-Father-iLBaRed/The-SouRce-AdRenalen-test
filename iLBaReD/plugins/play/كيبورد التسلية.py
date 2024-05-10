import asyncio
from pyrogram import Client, filters
from strings.filters import command
from iLBaReD.misc import SUDOERS
from iLBaReD.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,)
from iLBaReD import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

    
@app.on_message(filters.regex("‹ القائمة الرئيسية ›"), group=39)
@app.on_message(filters.regex("^/adrenalen"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )
    
REPLY_MESSAGE = "صلي علي النبي وتبسم ♥️☺️!"

REPLY_MESSAGE_BUTTONS = [
[("السورس"),("الاوامر")],
[("احرف"),("مطور السورس")],
[("تويت"),("صراحه")],
[("نكته"),("حكمه")],
[("انصحني"),("لو خيروك")],
[("‹ قسم الصور ›")],
[("‹ اغلاق الكيبورد ›")]]


#############################################################

@app.on_message(filters.command(["‹ قسم الصور ›"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["‹ صورة ›","‹ استوري ›"],["‹ جيف ›","‹ إنمي ›"],["‹ افتار شبابي ›","‹ افتار بناتي ›"],["‹ تواشيح النقشبندي ›","‹ استوري قران ›"],["‹ ايه قرآنيه عشوائي ›"],["‹ القائمة الرئيسية ›"]], resize_keyboard=True)
    await message.reply_text( "- مرحبا بك في قسم الصور ✨♥️ ،", reply_markup=kep)
 
  
#############################################################

@app.on_message(filters.regex("‹ اغلاق الكيبورد ›"))
async def down(client, message):
          m = await message.reply("تم اغلاق الكيبورد بنجاح 💘 ⋅ ", reply_markup= ReplyKeyboardRemove(selective=True))


    
    
