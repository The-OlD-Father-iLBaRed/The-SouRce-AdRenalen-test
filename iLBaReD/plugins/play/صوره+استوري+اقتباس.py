import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from iLBaReD import app
import random





lisetanme = []  
@Client.on_message(filters.command(["صور انمي", "صورة انمي", "صوره انمي", "انمي"], ""))
async def sssora(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(lisetanme) == 0:
     user = await get_userbot(client.me.username)
     async for msg in user.get_chat_history("LoreBots7"):
      if msg.media:
        lisetanme.append(msg)
  phot = random.choice(lisetanme)
  photo = f"https://t.me/LoreBots7/{phot.id}"
  await message.reply_photo(photo=photo, caption="**♪ 𝑱𝒐𝒊𝒏 ➧ @Elasyoutyyyy  💎 .**")




    

@app.on_message(command([f"صوره", "صورة", "صور"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/Picture_elnqyb/{phot.id}"
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




@app.on_message(command([f"استوريهات", "استوري", "استيت"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/videi_semo/{id}"
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


@app.on_message(command(["صوره انمي", "انمي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/LoreBots7/{phot.id}"
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
    
                                                              
@app.on_message(command(["استيكر", "متحركه"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/GifWaTaN/{rl}"
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
    

    
    
@app.on_message(command(["صور بنات", "افاتار بنات"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vvyuol/{rl}"
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
    
                            
@app.on_message(command(["صور شباب", "افاتار شباب"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vgbmm/{rl}"
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
    

@app.on_message(command(["سوره", "قرآن"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/opuml/{rl}"
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
                       
@app.on_message(command(["الشيخ", "النقشبندي", "نقشبندي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/ggcnjj/{rl}"
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

















