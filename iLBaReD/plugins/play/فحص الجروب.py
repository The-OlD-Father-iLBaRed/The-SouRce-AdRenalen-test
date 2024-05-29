import os
import time
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from strings.filters import command
from iLBaReD import app

@app.on_message(~filters.private & command(["/gdata","فحص الجروب"]), group=2)
async def instatus(app, message):
    photo = await app.download_media(message.chat.photo.big_file_id)
    start_time = time.perf_counter()
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    count = await app.get_chat_members_count(message.chat.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        sent_message = await message.reply_text("جاري تجميع البينات 💘 ⋅")
        deleted_acc = 0
        premium_acc = 0
        banned = 0
        bot = 0
        uncached = 0
        async for ban in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BANNED):
            banned += 1
        async for member in app.get_chat_members(message.chat.id):
            user = member.user
            if user.is_deleted:
                deleted_acc += 1
            elif user.is_bot:
                bot += 1
            elif user.is_premium:
                premium_acc += 1
            else:
                uncached += 1
        end_time = time.perf_counter()
        timelog = "{:.2f}".format(end_time - start_time)
        await message.reply_photo(photo=photo, caption=f"""
╭─《 • ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ • 》
├ -᚜ - اسم الـ جروب » ⦗ {message.chat.title} ⦘ 💘 ⋅ 
├ -᚜ - عدد الـ اعضاء » ⦗ {count} ⦘ 💘 ⋅ 
├ -᚜ - عدد الـ بوتات »  ⦗ {bot} ⦘ 💘 ⋅
├ -᚜ - عدد الـ حسبات الـ محذوفه » ⦗ {deleted_acc} ⦘ 💘 ⋅ 
├ -᚜ - عدد الـ مطرودين » ⦗ {banned} ⦘ 💘 ⋅
├ -᚜ - عدد الاغنية الي موثقين هنا » ⦗ {premium_acc} ⦘ 😂💘 ⋅
╰─《 • ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ • 》""")
    else:
        sent_message = await message.reply_text("يمكن للمسؤولين فقط!")
        await sleep(5)
        await sent_message.delete()
