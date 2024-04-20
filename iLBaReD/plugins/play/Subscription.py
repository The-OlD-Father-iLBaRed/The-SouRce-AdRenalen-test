from pyrogram import Client, filters
from pyrogram import enums
from pyrogram import types
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from iLBaReD import app

channel = "WA_ADRENALEN"
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: await app.get_chat_member(channel, user_id)
    except UserNotParticipant: return False
    return True
    
subscribed = filters.create(subscription)

@@app.on_message(~subscribed)
async def checker(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]: await message.delete()
    user_id = message.from_user.id
    user = message.from_user.first_name
    await message.reply(f"عذرًا عزيزي [{user}](tg://openmessage?user_id={user_id}) عليك الإشتراك بقناة البوت أولا.",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("‹ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ›", url=f"https://t.me/{channel}")]]
            ),parse_mode=enums.ParseMode.MARKDOWN)
