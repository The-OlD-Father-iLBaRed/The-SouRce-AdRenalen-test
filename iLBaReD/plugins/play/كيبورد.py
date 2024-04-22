import asyncio
from pyrogram import Client, filters
from strings.filters import command
from iLBaReD.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from iLBaReD import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "صلي علي النبي وتبسم ♥️☺️!"




REPLY_MESSAGE_BUTTONS = [
["السورس","الاوامر"],
["احرف","مطور السورس"],
["تويت","صراحه"],
["نكته","حكمه"],
["انصحني","لو خيروك"],
["حساب العمر","قسم الصور"],    
["‹ اغلاق الكيبورد ›"]]



@app.on_message(filters.regex("^/adrenalen","‹ القائمة الرئيسية ›"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

REPLY_MESSAGE = "- مرحبا بك في قسم الصور ✨♥️ ،"




REPLY_MESSAGE_BUTTONS = [
["‹ صوره ›","‹ استوري ›"],
["‹ استيكر ›","‹ انمي ›"],
["‹ افتار شباب ›","‹ افتار بنات ›"],
["‹ النقشبندي ›"],
["‹ اغلاق الكيبورد ›"]]



@app.on_message(filters.regex("قسم الصور"), group=40)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("‹ اغلاق الكيبورد ›"))
async def down(client, message):
          m = await message.reply("تم اغلاق الكيبورد بنجاح 💘   ⋅ ", reply_markup= ReplyKeyboardRemove(selective=True))
