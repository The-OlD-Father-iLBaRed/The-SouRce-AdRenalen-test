from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from iLBaReD import app
from config import OWNER_ID
from pyrogram.types import Message
from iLBaReD.utils.admin_check import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------------------------------------------------------------------- #


@app.on_message(filters.command(["تثبيت", "تثبيت الرسالة","ث"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("↢ وخر، ما يمديك تستخدم هالميزة بس في المجموعات.")
    elif not replied:
        await message.reply_text("↢ يجب الرد على الرسالة\n\n ༄")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"↢ أبشر ثبتت الرسالة\n\n ༄", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("شاهد الرسالة 📝", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command("pinned"))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("↢ ما في رسالة مُثبتة\n\n ༄")
    try:        
        await message.reply_text("↢ قائمة الرسائل المثبتة",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 عرض الرسالة",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["الغاء تثبيت","الغاء التثبيت"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("↢ وخر، ما يمديك تستخدم هالميزة بس في المجموعات.")
    elif not replied:
        await message.reply_text("↢ رد على الرسالة عشان يمديني ألغي تثبيتها")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"↢ أبشر لغيت تثبيت الرسالة\n\n༄", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("شاهد الرسالة 📝", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))
