from iLBaReD import app 
import asyncio
from pyrogram import enums
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []


The_TasRef = ["مشرفنا بحضور يـ ","@ل10 تشتريلي هدوم ونفطر سوا ؟",
"@ل1 قولو با ايه مستفاد منك ؟",
"@ل2 قولو با ايه مستفاد منك ؟",
"@ل3 قولو با ايه مستفاد منك ؟",
"@ل4 قولو با ايه مستفاد منك ؟",
"@ل5 قولو با ايه مستفاد منك ؟",
"@ل6 قولو با ايه مستفاد منك ؟",
"@ل7 قولو با ايه مستفاد منك ؟",
"@ل8 قولو با ايه مستفاد منك ؟",
"@ل9 قولو با ايه مستفاد منك ؟",
"@ل10 قولو با ايه مستفاد منك ؟",
"@ل1 قولو تحبني",
"@ل2 قولو تحبني",
"@ل3 قولو تحبني",
"@ل4 قولو تحبني",
"@ل5 قولو تحبني",
"@ل6 قولو تحبني",
"@ل7 قولو تحبني",
"@ل8 قولو تحبني",
"@ل9 قولو تحبني",
"@ل10 قولو تحبني",
"@ل1 قولو اسألني سؤال",
"@ل2 قولو اسألني سؤال",
"@ل3 قولو اسألني سؤال",
"@ل4 قولو اسألني سؤال",
"@ل5 قولو اسألني سؤال",
"@ل6 قولو اسألني سؤال",
"@ل7 قولو اسألني سؤال",
"@ل8 قولو اسألني سؤال",
"@ل9 قولو اسألني سؤال",
"@ل10 قولو اسألني سؤال",
"@ل1 قولو اغنية لطيفة",
"@ل2 قولو اغنية لطيفة",
"@ل3 قولو اغنية لطيفة",
"@ل4 قولو اغنية لطيفة",
"@ل5 قولو اغنية لطيفة",
"@ل6 قولو اغنية لطيفة",
"@ل7 قولو اغنية لطيفة",
"@ل8 قولو اغنية لطيفة",
"@ل9 قولو اغنية لطيفة",
"@ل10 قولو اغنية لطيفة",
"@ل1 قولو نتجوز",
"@ل2 قولو نتجوز",
"@ل3 قولو نتجوز",
"@ل4 قولو نتجوز",
"@ل5 قولو نتجوز",
"@ل6 قولو نتجوز",
"@ل7 قولو نتجوز",
"@ل8 قولو نتجوز",
"@ل9 قولو نتجوز",]



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
            txt = f"{usrtxt} {random.choice(The_TasRef)} 😋♥️ ،"
            await app.send_message(chat_id, txt)
            await asyncio.sleep(4)
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
