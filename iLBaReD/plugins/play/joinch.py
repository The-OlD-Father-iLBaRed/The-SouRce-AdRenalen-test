import yt_dlp
import os
import asyncio
from typing import Union
from pyrogram import Client, filters
from pyrogram import Client as client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import appp, OWNER, OWNER_NAME, VIDEO

async def joinch(message):
        ii = await must_join(message._client.me.username)
        if ii == "معطل":
          return
        cch = await get_channel(message._client.me.username)
        ch = cch.replace("https://t.me/HLV_M")
        try:
            await message._client.get_chat_member(ch, message.from_user.id)
        except UserNotParticipant:
            try:
                await message.reply(
                    f"🚦 يجب ان تشترك في القناة\n\nقنـاة الـبـوت : « {cch} »",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("اضـغط هنا للأشتـراك القنـاة 🚦", url=f"{cch}"),
                            ],
                         ] 
                      ) 
                   )
                return True
            except Exception as a:
                print(a)
        except Exception as a:
              print(a)
