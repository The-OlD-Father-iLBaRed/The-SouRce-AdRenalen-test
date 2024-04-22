import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import app
import random
    

@app.on_message(command(["صوره","‹ صورة ›"]))
async def Soraa(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )


                       
@app.on_message(command(["النقشبندي","‹ النخشبندي تواشيح ›"]))
async def elnaqsbnde(client: Client, message: Message):
    rl = random.randint(2,51)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_photo(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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
async def stats(client: Client, message: Message):
    rl = random.randint(2,52)
    url = f"https://t.me/yoipopl{rl}"
    await client.send_photo(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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
    rl = random.randint(2,53)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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
    rl = random.randint(2,54)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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
    rl = random.randint(2,55)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_photo(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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
async def gef(client: Client, message: Message):
    rl = random.randint(2,55)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_photo(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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