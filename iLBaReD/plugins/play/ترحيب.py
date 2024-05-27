from pyrogram import Client as app, filters,enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup as mk, InlineKeyboardButton as btn
from pyrogram.types import ChatPermissions
from asSQL import Client as cl

data = cl("protect")
db = data['data']
@app.on_chat_member_updated()
@app.on_message(filters.new_chat_members)
def welcome(app,message):
    chat_id = message.chat.id
    m = message.from_user.mention
    km = f"""
لا تُسِئ اللفظ وإن ضَاق عليك الرَّد

ɴᴀᴍᴇ ⌯ ⁪⁬⁪⁬{m}
𝖣𝖺𝗍𝖾 ⌯ {message.date}
"""
    k = db.get(f"group_{message.chat.id}_welcome")
    if db.get(f"lock_welcome_{message.chat.id}") == False:
        if k == None:
            app.send_message(chat_id,km)
        else:
            kc = db.get(f"group_{message.chat.id}_welcome")
            message.reply(chat_id,kc)




@app.on_message(filters.new_chat_members, group=7130)
async def welcome(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
        m = await app.get_users(int(x[0]))
        chatid = message.chat.id
        photo = await client.download_media(message.chat.photo.big_file_id)
        bot_username = (await app.get_me()).username
        await app.send_photo(
            chatid, 
            photo=photo, 
            caption=f"- نورت ياا قمر 🌗😘🤝️ {message.from_user.mention}\n│ \n└ʙʏ في {message.chat.title}",     
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("مـالـك الـجـروب⚡", url=f"https://t.me/{m.username}")], 
                [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{app.username}?startgroup=True")]
            ]))
            
            
            
@app.on_message(filters.left_chat_member, group=7130)
async def goodbye(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
        m = await app.get_users(int(x[0]))
        chatid = message.chat.id
        photo = await client.download_media(message.chat.photo.big_file_id)
        bot_username = (await app.get_me()).username
        await app.send_photo(
            chatid, 
            photo=photo, 
            caption=f"- مشيت ليه يقلبي يلا بسلامات🥲👋\n│ \n└ʙʏ  {message.from_user.mention} ",     
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("مـالـك الـجـروب⚡", url=f"https://t.me/{m.username}")], 
                [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{app.username}?startgroup=True")]
            ]))
