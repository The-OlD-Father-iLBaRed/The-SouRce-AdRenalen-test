import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from iLBaReD import app

# ------------------------------------------------------------------------------- #

chatQueue = []

stopProcess = False

# ------------------------------------------------------------------------------- #


        
@app.on_message(filters.command(["مسح الحسابات المحذوفة"], ""))
async def remove(client, message):
  global stopProcess
  try: 
    try:
      sender = await app.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      bot = await app.get_chat_member(message.chat.id, "self")
      if bot.status == ChatMemberStatus.MEMBER:
        await message.reply("**↢ كيف أمسح الحسابات المحذوفة وما معي صلاحية حظر الأعضاء؟")  
      else:  
        if len(chatQueue) > 30 :
          await message.reply("↢ أنا مستعد للعمل، عيد المحاولة.")
        else:  
          if message.chat.id in chatQueue:
            await message.reply("↢ التنظيف يجري بالفعل..")
          else:  
            chatQueue.append(message.chat.id)  
            deletedList = []
            async for member in app.get_chat_members(message.chat.id):
              if member.user.is_deleted == True:
                deletedList.append(member.user)
              else:
                pass
            lenDeletedList = len(deletedList)  
            if lenDeletedList == 0:
              await message.reply("↢ما فيه حسابات محذوفة.")
              chatQueue.remove(message.chat.id)
            else:
              k = 0
              processTime = lenDeletedList*1
              temp = await app.send_message(message.chat.id, f"↢ عدد الحسابات المحذوفة {lenDeletedList} تم إزالة جميع الحسابات المحذوفة\n↢ الوقت المُستغرق : {processTime} ثانية.")
              if stopProcess: stopProcess = False
              while len(deletedList) > 0 and not stopProcess:   
                deletedAccount = deletedList.pop(0)
                try:
                  await app.ban_chat_member(message.chat.id, deletedAccount.id)
                except Exception:
                  pass  
                k+=1
                await asyncio.sleep(10)
              if k == lenDeletedList:  
                await message.reply(f"**↢ تم حذف الحسابات المحذوفة.")  
                await temp.delete()
              else:
                await message.reply(f"↢ تم حذف {k} حساب محذوف من هذه المجموعة")  
                await temp.delete()  
              chatQueue.remove(message.chat.id)
    else:
      await message.reply("↢ ما يمديك تستخدم هالأمر أنت مو مُشرف")  
  except FloodWait as e:
    await asyncio.sleep(e.value)                               
