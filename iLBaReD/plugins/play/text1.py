from iLBaReD import app
from pyrogram import enums
from pyrogram import filters
from pyrogram import Client
from strings.filters import command
import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

developer_id = 1924832439  

@app.on_message(
    filters.command("تخ") & filters.user(developer_id)
)
async def respond_to_developer(client: Client, message: Message):
    await message.reply_text("أنت عبيط عايز تموت المطور")

@app.on_message(
    command(["تخ"])
)
async def huhh(client: Client, message: Message):
    # آيدي الشخص الذي عمل عليه رد الريبلي
    replied_user_id = message.reply_to_message.from_user.id
    replied_user_name = message.reply_to_message.from_user.first_name
    # آيدي الشخص الذي قام بإرسال رد الريبلي
    killer_id = message.from_user.id
    killer_name = message.from_user.first_name
    await message.reply_video(
        video=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
        caption=f"القاتل هو: [{killer_name}](tg://user?id={killer_id})\nالضحية هو: [{replied_user_name}](tg://user?id={replied_user_id})\nانا لله وانا اليه راجعون 😥😥",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "خــودنــي لــجروبك🥺💗", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
            ]
        ),
        parse_mode=enums.ParseMode.MARKDOWN
    )
