from pyrogram import Client, filters, idle
from config import OWNER
from iLBaReD.plugins.additions.pv_adrenalen import (is_served_user, add_served_user)
from iLBaReD.plugins.additions.pv_adrenalen import (get_dev)
from iLBaReD.__init__ import (AdRenalen_SubScRip)
from pyrogram.types import Message


OFFPV = []

@Client.on_message(filters.command(["تفعيل التواصل","تعطيل التواصل"], ""))
async def byyye(client, message):
    user = message.from_user.username
    dev = await get_dev(client.me.username)
    if user in OWNER or message.from_user.id == dev:
        text = message.text
        if text == "تفعيل التواصل":
          if not client.me.username in OFFPV:
             await message.reply_text("**التواصل مفعل من قبل .**")
          try:
            OFFPV.remove(client.me.username)
            await message.reply_text("**تم تفعيل التواصل .**")
            return
          except:
             pass
        if text == "تعطيل التواصل":
          if client.me.username in OFFPV:
             await message.reply_text("**التواصل معطل من قبل .**")
          try:
            OFFPV.append(client.me.username)
            await message.reply_text("**تم تعطيل التواصل .**")
            return
          except:
             pass


@Client.on_message(filters.private)
async def botoot(client: Client, message: Message):
 if not client.me.username in OFFPV:
  if await AdRenalen_SubScRip(message):
            return
  bot_username = client.me.username
  user_id = message.chat.id
  if not await is_served_user(client, user_id):
     await add_served_user(client, user_id)
  dev = await get_dev(bot_username)
  if message.from_user.id == dev or message.chat.username in OWNER or message.from_user.id == client.me.id:
    if message.reply_to_message:
     u = message.reply_to_message.forward_from
     try:
       await client.send_message(u.id, text=message.text)
       await message.reply_text(f"**تم ارسال رساتلك إلي {u.mention} بنجاح .**")
     except Exception:
         pass
  else:
   try:
    await client.forward_messages(dev, message.chat.id, message.id)
    await client.forward_messages(OWNER[0], message.chat.id, message.id)
   except Exception as e:
     pass
 message.continue_propagation()
 
 
 
 
 
 
async def is_served_user(client, user_id: int) -> bool:
    userdb = await get_data(client)
    userdb = userdb.users
    user = await userdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True
    
async def add_served_user(client, user_id: int):
    userdb = await get_data(client)
    userdb = userdb.users
    is_served = await is_served_user(client, user_id)
    if is_served:
        return
    return await userdb.insert_one({"user_id": user_id})
    
async def del_served_user(client, user_id: int):
    chats = await get_data(client)
    chatsdb = chats.users
    is_served = await is_served_user(client, user_id)
    if not is_served:
        return
    return await chatsdb.delete_one({"user_id": user_id})
    
async def get_dev(bot_username):
  devv = dev.get(bot_username)
  if not devv:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         devo = i["dev"]
         dev[bot_username] = devo
         return devo
  return devv

# Developer Name
async def get_dev_name(client, bot_username):
  devv = devname.get(bot_username)
  if not devv:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         devo = i["dev"]
         devo = await client.get_chat(devo)
         devo = devo.first_name
         devname[bot_username] = devo
         return devo
  return devv



async def get_dev(bot_username):
  devv = dev.get(bot_username)
  if not devv:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         devo = i["dev"]
         dev[bot_username] = devo
         return devo
  return devv

# Developer Name
async def get_dev_name(client, bot_username):
  devv = devname.get(bot_username)
  if not devv:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         devo = i["dev"]
         devo = await client.get_chat(devo)
         devo = devo.first_name
         devname[bot_username] = devo
         return devo
  return devv
  
  async def get_dev_user(bot_username):
      name = devuserr.get(bot_username)
      if not name:
        dev = dev_userr.find_one({"bot_username": bot_username})
        if not dev:
            return "E_Z_9"
        devuserr[bot_username] = dev["dev_userr"]
        return dev["dev_userr"]
      return name
