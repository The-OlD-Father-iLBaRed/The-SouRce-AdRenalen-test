from iLBaReD import app 
import asyncio
from pyrogram import enums
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []


The_TasRef = ["مشرفنا بحضور يـ "]



@app.on_message(filters.command(["تفعيل التشريف"], prefixes=["", "@", "#"]))
async def mention_allvc(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("- تم تفعيل التشريف ويتم ارسال التشريفات كل اربع سعات من الان 😋♥️ ،")
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("- هذا الامر في الجروبات فقط 😋♥️ ،")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("- هذا الامر للمشرفين فقط 😋♥️ ،")
    if chat_id in spam_chats:
        return await message.reply("- التشريف مفعل من قبل 😋♥️ ،")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id})"

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(The_TasRef)} 😋♥️ ،",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        usr.user.first_name, url=f"https://t.me/{usrtxt}"),
                ],
            ],),
        parse_mode=enums.ParseMode.MARKDOWN)
            await app.send_message(chat_id, txt)
            await asyncio.sleep(14400)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["تعطيل التشريف"], prefixes=["", "@", "#"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("- التشريف معطل من قبل 😋♥️ ،")
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("- هذا الامر في الجروبات فقط 😋♥️ ،")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("- هذا الامر للمشرفين فقط 😋♥️ ،")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("- تم تعطيل التشريف بنجاح 😋♥️ ،")
