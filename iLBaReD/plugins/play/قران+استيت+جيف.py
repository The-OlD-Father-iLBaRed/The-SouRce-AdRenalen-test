import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import app
import random
    

@app.on_message(command(["سورة عشوائية","‹ قرآن عشوائي ›"]))
async def Soraa(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/alkoraan4000/{rl}"
    await client.send_audio(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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
