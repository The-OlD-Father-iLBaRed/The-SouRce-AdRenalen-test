from strings.filters import command
from iLBaReD import app
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

bad_words = []

@app.on_message(filters.command(["قفل السب","تعطيل السب"],""))
async def block_bad_words(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in bad_words:
            return await message.reply_text(f"تم قفل السب من قبل 😋♥️ ،")
        bad_words.append(message.chat.id)
        return await message.reply_text(f"قام : ⦗ {message.from_user.mention} ⦘\nبقفل السب 😋♥️ ،")
    else:
        return await message.reply_text(f"- انت لسته مشرف يـ ⦗ {message.from_user.mention} ⦘\nوهذا الامر للمشرفين 😋♥️ ،")
        
@app.on_message(filters.command(["فتح السب","تفعيل السب"],""))
async def unblock_bad_words(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in bad_words:
            return await message.reply_text(f"تم فتح السب من قبل 😋♥️ ،")
        bad_words.remove(message.chat.id)
        return await message.reply_text(f"قام : ⦗ {message.from_user.mention} ⦘\n بفتح السب 😋♥️ ،")
    else:
        return await message.reply_text(f"- انت لسته مشرف يـ ⦗ {message.from_user.mention} ⦘\nوهذا الامر للمشرفين 😋♥️ ،")

@app.on_message(filters.bad_words)
async def delete_bad_words(client:Client, message:Message):
    if message.chat.id in bad_words:
        await message.delete()
        await message.reply(f"عزرا يـ  ⦗ {message.from_user.mention} ⦘ 😋♥️ ،\nلا يمكنك ارسال كلمات مسيئة هنا 😋♥️ ،")       
   
