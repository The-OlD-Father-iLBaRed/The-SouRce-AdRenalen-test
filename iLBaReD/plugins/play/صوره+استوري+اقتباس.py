import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import app
import random
    

@app.on_message(command(["صوره","‹ صورة ›"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,60)
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



@app.on_message(command(["استوريهات", "استيت","‹ استوري ›"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,70)
    url = f"https://t.me/yoipopl{rl}"
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


@app.on_message(command(["انمي","‹ إنمي ›"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,80)
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
    
                                                              
@app.on_message(command(["استيكر","‹ جيف ›"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
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
    

    
    
@app.on_message(command(["افتار بنات","‹ افتار بناتي ›"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,00)
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
async def ihd(client: Client, message: Message):
    rl = random.randint(3,10)
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
    
                       
@app.on_message(command(["النقشبندي","‹ النقشبندي تواشيح ›"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,20)
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
