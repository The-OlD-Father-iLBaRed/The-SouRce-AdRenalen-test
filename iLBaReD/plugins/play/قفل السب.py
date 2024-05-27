from iLBaReD import app
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

The_BadWord_Bot = []

The_BadWord = ["زي صحبك","بوت عرص","زبي عليك","زبي فيك","لحاس النسوان","بز","كس","كسمك","كسختك","عير","كسخالتك","خرا بالله","عير بالله","كسخواتكم","كحاب","مناويج","مناويج","كحبه","ابن الكحبه","فرخ","فروخ","طيزك","طيزختك","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","ابن العرص","منايك","متناك","احا","ابن المتناكه","زبك","عرص","زبي","خول","لبوه","لباوي","ابن اللبوه","منيوك","كسمكك","متناكه","احو","احي","يا عرص","يا خول","قحبه","القحبه","شراميط","العلق","العلوق","العلقه","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","االمنيوك","كسمككك","الشرموطه","ابن العرث","ابن الحيضانه","زبك","خول","زبي","قاحب","تيزك","اختك لبوة","اوعي ترمي ااختك علي زبي ","امك الهيجة ","يبن ال شرموطة","يبن الـ شرموطة ","يلي امك فجره","طيازك"]
  
@app.on_message(filters.command(["قفل السب","تعطيل السب"],""))
async def block_The_BadWord(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in The_BadWord_Bot:
            return await message.reply_text(f"- تم قفل السب من قبل 😋♥️ ،")
        The_BadWord_Bot.append(message.chat.id)
        return await message.reply_text(f"قام : ⦗ {message.from_user.mention} ⦘\nبقفل السب 😋♥️ ،")
    else:
        return await message.reply_text(f"- انت لسته مشرف يـ ⦗ {message.from_user.mention} ⦘\nوهذا الامر للمشرفين 😋♥️ ،")

@app.on_message(filters.command(["فتح السب","تفعيل السب"],""))
async def unblock_The_BadWord(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in The_BadWord_Bot:
            return await message.reply_text(f"تم فتح السب من قبل 😋♥️ ،")
        The_BadWord_Bot.remove(message.chat.id)
        return await message.reply_text(f"قام : ⦗ {message.from_user.mention} ⦘\n بفتح السب 😋♥️ ،")
    else:
        return await message.reply_text(f"- انت لسته مشرف يـ ⦗ {message.from_user.mention} ⦘\nوهذا الامر للمشرفين 😋♥️ ،")
@app.on_message(The_BadWord)
async def delete_The_BadWord(client:Client, message:Message):
    if message.chat.id in The_BadWord_Bot:
        await message.delete()
        await message.reply(f"لا يمكنك ارسال كلمات مسيئة هنا 😋♥️ ،")
