import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import app
import random
    

@app.on_message(command(["صوره","‹ صورة ›"]))
async def Soraa(client: Client, message: Message):
    rl = random.randint(2,50)
    photo = f"https://t.me/Picture_elnqyb/{rl}"
    await message.reply_photo(photo=photo, caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
    reply_to_message_id=message.id,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
                           
                           
@app.on_message(command(["انمي","‹ إنمي ›"]))
async def inme(client: Client, message: Message):
    rl = random.randint(2,51)
    photo = f"https://t.me/ienamee/{rl}"
    await message.reply_photo(photo=photo, caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
    reply_to_message_id=message.id,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
                           
                                   
@app.on_message(command(["افتار بنات","‹ افتار بناتي ›"]))
async def avtar(client: Client, message: Message):
    rl = random.randint(2,52)
    photo = f"https://t.me/vvyuol/{rl}"
    await message.reply_photo(photo=photo, caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
    reply_to_message_id=message.id,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
                           
                                                                               
@app.on_message(command(["افتار شباب","‹ افتار شبابي ›"]))
async def avtarto(client: Client, message: Message):
    rl = random.randint(2,53)
    photo = f"https://t.me/vgbmm/{rl}"
    await message.reply_photo(photo=photo, caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
    reply_to_message_id=message.id,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
                           
                           
@app.on_message(command(["سورة عشوائية","‹ استوري قران ›"]))
async def soraa(client, message): 
    rl = random.randint(2,54)
    video = f"https://t.me/a9li91/{rl}"
    await message.reply_video(video=video, caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
    reply_to_message_id=message.id,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
                           
                         
@app.on_message(command(["‹ جيف ›","استيكر"]))
async def soraa(client, message): 
    rl = random.randint(2,55)
    video = f"https://t.me/GifWaTaN/{rl}"
    await message.reply_video(video=video, caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
    reply_to_message_id=message.id,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
                           

@app.on_message(command(["استيت","‹ استوري ›"]))
async def soraa(client, message): 
    rl = random.randint(2,56)
    video = f"https://t.me/yoipopl/{rl}"
    await message.reply_video(video=video, caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
    reply_to_message_id=message.id,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
                                                      

@app.on_message(command(["النقشبندي","‹ تواشيح النقشبندي ›"]))
async def soraa(client, message): 
    rl = random.randint(2,57)
    audio = f"https://t.me/ggcnjj/{rl}"
    await message.reply_audio(audio=audio, caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
    reply_to_message_id=message.id,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
                           
                           
@app.on_message(command(["ايه قرآنيه","‹ ايه قرآنيه عشوائي ›"]))
async def soraa(client, message): 
    rl = random.randint(2,58)
    audio = f"https://t.me/UQII9/{rl}"
    await message.reply_audio(audio=audio, caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
    reply_to_message_id=message.id,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
 
