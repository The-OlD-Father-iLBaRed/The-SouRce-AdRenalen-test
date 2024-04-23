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


@app.on_message(filters.regex("‹ قسم الصور ›"), group=40)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )
REPLY_MESSAGE = "- مرحبا بك في قسم الصور ✨♥️ ،"

REPLY_MESSAGE_BUTTONS = [
[("‹ صورة ›"),("‹ استوري ›")],
[("‹ جيف ›"),("‹ إنمي ›")],
[("‹ افتار شبابي ›"),("‹ افتار بناتي ›")],
[("‹ النقشبندي تواشيح ›"),("‹ استوري قران ›")],
[("‹ القائمة الرئيسية ›")],
[("‹ اغلاق الكيبورد ›")]]

