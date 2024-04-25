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



 ##############
@app.on_message(command(["تخ","بيو"]))
async def Katl(client: Client, message: Message):
    if message.reply_to_message.from_user.id == 1924832439:
        await message.reply("لا يمكنك قتل مطور السورس ي غبي 😋♥️ ،")
    elif message.reply_to_message.from_user.id == message.from_user.id:
        await message.reply("لا يمكنك قتل نفسك")
    elif message.reply_to_message.from_user.id == app.id:
        await message.reply("لا يمكنك قتل البوت")
    else:
        # آيدي الشخص الذي عمل عليه رد الريبلي
        replied_user_id = message.reply_to_message.from_user.id
        replied_user_name = message.reply_to_message.from_user.first_name
        # آيدي الشخص الذي قام بإرسال رد الريبلي
        killer_id = message.from_user.id
        killer_name = message.from_user.first_name
        await message.reply_video(
            video=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
            caption=f"- القاتل المفتري » ⦗ {killer_name} (tg://user?id={killer_id}) ⦘\n- المقتول بمسدس مايه » ⦗ {replied_user_name} (tg://user?id={replied_user_id}) ⦘ \nانا لله وانا اليه راجعون الواد مات بمسدس لعبه 😂!",
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
