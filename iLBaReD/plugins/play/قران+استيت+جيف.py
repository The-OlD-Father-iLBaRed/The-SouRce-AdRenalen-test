import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import app
import random
    

@app.on_message(command(["سورة عشوائية","‹ قرآن عشوائي ›"]))
async def soraa(client, message):
 if len(listvidquran) == 0:
    audi = random.choice(listvidquran)
    audio = f"https://t.me/a9li91/{audi}"
    await message.reply_audio(audio=audio, caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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
    await message.reply_video(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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
    await message.reply_video(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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
    await message.reply_audio(message.chat.id,url,caption="- Join.Channel.SouRce : @WA_ADRENALEN ⋅",
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
