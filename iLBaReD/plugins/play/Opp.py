import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from iLBaReD import app
from typing import Union
from pyrogram.types import InlineKeyboardButton

The_Stayle_Pic = ["صورتك رايقة يصحبي","صورتك حلوة شوية","اي وشك دا يقطع الخميرة من البيت","تلاق تلاتة اتخديت من مالك","صورتك دي ولا القمر","عايز اتصور صورة معاك","انتا فجمال جورجينا","متحولش تغريني بغمزاتك","صورتك تشبه القمر"]

@app.on_message(filters.command(["صورتي","ص"], ""))
async def madison(client: Client, message: Message):
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
