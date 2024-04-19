import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from iLBaReD import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from iLBaReD import app
from random import  choice, randint
from pyrogram import enums
from pyrogram import types
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from asyncio import gather
from pyrogram import Client, filters
from pyrogram import enums
from pyrogram import types
import aiohttp
from pyrogram.types import CallbackQuery
from pyrogram.enums import ChatMemberStatus
from iLBaReD import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from asyncio import gather
from pyrogram.errors import FloodWait

@app.on_message(command(["تخ"]))
async def huhh(client: Client, message: Message):
    try:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user_name = message.reply_to_message.from_user.first_name
        killer_id = message.from_user.id
        killer_name = message.from_user.first_name
        await message.reply_video(
            video=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
            caption=f"القاتل هو: {killer_name}\nالضحية هو: {replied_user_name}\nانا لله وانا اليه راجعون 😥😥",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "خــودنــي لــجروبك🥺💗", url=f"https://t.me/{app.username}?startgroup=true"),
                    ],
                ]
            ),
            parse_mode=enums.ParseMode.MARKDOWN
        )
    except Exception as e:
        if message.from_user.id == 1924832439:  # ايدي المطور
            msg_text = "↢ كيف تبيني اتف علي مطوري "
            await client.send_message(message.from_user.id, msg_text)
