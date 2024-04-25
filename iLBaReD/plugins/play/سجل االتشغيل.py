from pyrogram.enums import ParseMode
from iLBaReD import app
from strings.filters import command
from iLBaReD.utils.database import is_on_off
from config import OWNER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>

<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>
<b>ᴄʜᴀᴛ ɴᴀᴍᴇ :</b> {message.chat.title}
<b>ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}

<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>
<b>ɴᴀᴍᴇ :</b> {message.from_user.mention}
<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}
<b>ǫᴜᴇʀʏ :</b> {message.text.split(None, 1)[1]}
<b>sᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}"""
        if message.chat.id != OWNER_ID:
            try:
                await app.send_message(
                    chat_id=OWNER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return


@app.on_message(filters.command(["صلاحياتي"], ""))
async def caesarprivileges(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    cae = await client.get_chat_member(chat_id, user_id)
    status = cae.status if cae else None
    if status == ChatMemberStatus.OWNER:
        await message.reply_text("أنت مالك الجروب")
    elif status == ChatMemberStatus.MEMBER:
        await message.reply_text("أنت عضو حقير")
    else:
        privileges = cae.privileges if cae else None 
        can_promote_members = "✅" if (privileges and privileges.can_promote_members) else "❌"
        can_manage_video_chats = "✅" if (privileges and privileges.can_manage_video_chats) else "❌"
        can_pin_messages = "✅" if (privileges and privileges.can_pin_messages) else "❌"
        can_invite_users = "✅" if (privileges and privileges.can_invite_users) else "❌"
        can_restrict_members = "✅" if (privileges and privileges.can_restrict_members) else "❌"
        can_delete_messages = "✅" if (privileges and privileges.can_delete_messages) else "❌"
        can_change_info = "✅" if (privileges and privileges.can_change_info) else "❌"
        hossam = f"صلاحياتك في الجروب:\n\n"
        hossam += f"ترقية الأعضاء: {can_promote_members}\n"
        hossam += f"إدارة الدردشات الصوتية: {can_manage_video_chats}\n"
        hossam += f"تثبيت الرسائل: {can_pin_messages}\n"
        hossam += f"دعوة المستخدمين: {can_invite_users}\n"
        hossam += f"تقييد الأعضاء: {can_restrict_members}\n"
        hossam += f"حذف الرسائل: {can_delete_messages}\n"
        hossam += f"تغيير معلومات الجروب: {can_change_info}\n"
        await message.reply_text(hossam)
