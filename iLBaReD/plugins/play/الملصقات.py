from iLBaReD import app
from pyrogram import enums
from pyrogram import Client
from strings.filters import command
import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from iLBaReD import app
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

stiklok = []

@app.on_message(filters.command(["قفل الملصقات","تعطيل الملصقات"],""))
async def block_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مقفلة من قبل")
        stiklok.append(message.chat.id)
        return await message.reply_text(f"تم قفل الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.command(["فتح الملصقات","تفعيل الملصقات"],""))
async def unblock_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in stiklok:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مفتوحة من قبل")
        stiklok.remove(message.chat.id)
        return await message.reply_text(f"تم فتح الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.sticker)
async def delete_stickers(client:Client, message:Message):
    if message.chat.id in stiklok:
        await message.delete()
        await message.reply(f"لا يمكنك ارسال الملصقات هنا 😋♥️ ، {message.from_user.mention}")

 ##############
@app.on_message(command(["تخ","بيو"]))
async def Katl(client: Client, message: Message):
    if message.reply_to_message.from_user.id == 1924832439:
        await message.reply("لا يمكنك قتل مطور السورس ي غبي 😋♥️ ،")
    else:
        # آيدي الشخص الذي عمل عليه رد الريبلي
        replied_user_id = message.reply_to_message.from_user.id
        replied_user_name = message.reply_to_message.from_user.first_name
        # آيدي الشخص الذي قام بإرسال رد الريبلي
        killer_id = message.from_user.id
        killer_name = message.from_user.first_name
        await message.reply_video(
            video=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
        caption=f"- القاتل المفتري » ⦗ [{killer_name}](tg://user?id={killer_id}) ⦘\n- المقتول بمسدس مايه » ⦗ [{replied_user_name}](tg://user?id={replied_user_id}) ⦘ \nانا لله وانا اليه راجعون الواد مات بمسدس لعبه 😂!",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "- ضفني في جروبك يرايق 😋♥️ ،", url=f"https://t.me/{app.username}?startgroup=true"),
                    ],
                ]
            ),
            parse_mode=enums.ParseMode.MARKDOWN
        )
