import asyncio
import os
import time
import requests
from pyrogram import enums
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from iLBaReD  import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from iLBaReD  import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from random import choice
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from iLBaReD import app
from typing import Union
from pyrogram.types import InlineKeyboardButton


menchen_all_chat = []
@app.on_message(filters.command(["@all", "تاك","all"], "") & ~filters.private, group=88)
async def nummmm(client: app, message):
  if message.chat.id in menchen_all_chat:
        return await message.reply_text("صورتي معطل اطلب من المشرفين تفتحه 😋♥️ ،")
  elif message.chat.id in menchen_all_chat:
     return await message.reply_text("التاك قيد التشغيل الان 💘 ⋅")
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("الامر دا للمشرفين بس 💘 ⋅")
    return
  await message.reply_text("جار بدء المنشن لايقاف التشغيل اكتب ⦗ ايقاف التاك ⦘ 💘 ⋅")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("all","")
  except:
    pass
  menchen_all_chat.append(message.chat.id)
  async for x in client.get_chat_members(message.chat.id):
      if message.chat.id not in menchen_all_chat:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ›"
       if i == 50:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 250:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              menchen_all_chat.remove(message.chat.id)
  menchen_all_chat.remove(message.chat.id)


@app.on_message(filters.command(["ايقاف المنشن","تعطيل المنشن","/cancel", "ايقاف التاك"], ""), group=822)
async def stop(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("الامر دا للمشرفين بس 💘 ⋅")
    return
  if message.chat.id not in menchen_all_chat:
     await message.reply("المنشن متوقف يصحبي 💘 ⋅")
     return 
  if message.chat.id in menchen_all_chat:
    menchen_all_chat.remove(message.chat.id)
    await message.reply("تم ايقاف المنشن يزميلي 💘 ⋅")
    return

