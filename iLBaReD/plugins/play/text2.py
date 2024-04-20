from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from iLBaReD import app
from config import OWNER_ID
from pyrogram.types import Message
from iLBaReD.utils.iLBaReD_Pin import admin_filter
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
        await message.reply_text("-᚜ - » ⦗ هذه الميزه في المجموعات فقط ⦘ 💘 ⋅ ")
    elif not replied:       
        await message.reply_text("-᚜ - » ⦗ عليك الرد علي رسالة ⦘ 💘 ⋅ ")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text("- تم تثبيت الرسالة 💘 ⋅ ")
            except Exception as e:
                await message.reply_text(str(e))
                
# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["الغاء تثبيت"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("-᚜ - » ⦗ هذه الميزه في المجموعات فقط ⦘ 💘 ⋅ ")
    elif not replied:
        await message.reply_text("-᚜ - » ⦗ عليك الرد علي رسالة لالغاء التثبيت ⦘ 💘 ⋅ ")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text("- تم الغاء تثبيت الرسالة 💘 ⋅ ")
            except Exception as e:
                await message.reply_text(str(e))




# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["مسح صوره المجموعه"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("-᚜ - » ⦗ جاري مسح صورة المجموعه  ⦘ 💘 ⋅ ")
      iLBaReD_Pin = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("- الامر دا للمجموعات بس  💘 ⋅ ")
      try:
         if iLBaReD_Pin.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)            
             await msg.edit("-᚜ - تم حذف صورة المجموعة 💘 ⋅\nمن قام بحذف الصورة » ⦗ {} ⦘ 💘 ⋅ ".format(message.from_user.mention))
      except:
          await msg.edit("-᚜ - » ⦗ أحتاج إلى صلاحية تعديل معلومات المجموعة ⦘ 💘 ⋅ ")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(["وضع صوره", "تغير صوره"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("-᚜ - » ⦗ جاري تغير صورة المجموعه  ⦘ 💘 ⋅ ")
      iLBaReD_Pin = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("- الامر دا للمجموعات بس  💘 ⋅ ")
      elif not reply:
           await msg.edit("-᚜ - » ⦗ عليك الرد علي صوره للتغير ⦘ 💘 ⋅ ")
      elif reply:
          try:
             if iLBaReD_Pin.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("- تم تغير صورة المجموعة  💘 ⋅ \n- ذوئك حلو خلي بالك يا ⦗ {} ⦘ 💘 ⋅".format(message.from_user.mention))
             else:
                await msg.edit("- هناك مشكلة قم بئرسال صورة اخري او المحاولة من جديد  💘 ⋅")
                
     
          except:            
              await msg.edit("-᚜ - » ⦗ أحتاج إلى صلاحية تعديل معلومات المجموعة ⦘ 💘 ⋅ ")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["وضع اسم", "تغير اسم الجروب"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("-᚜ - » ⦗ جاري تغير اسم المجموعه  ⦘ 💘 ⋅ ")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("- الامر دا للمجموعات بس  💘 ⋅ ")
    elif reply:
          try:
            title = message.reply_to_message.text
            iLBaReD_Pin = await app.get_chat_member(chat_id, user_id)
            if iLBaReD_Pin.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("-᚜ - تم تغير اسم المجموعة 💘 ⋅\nمن قام بتغير الاسم » ⦗ {} ⦘ 💘 ⋅ ".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("- اعطيني صلاحة تعديل المجموعة لكي اقوم بتغير الاسم  💘 ⋅")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            iLBaReD_Pin = await app.get_chat_member(chat_id, user_id)
            if iLBaReD_Pin.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("-᚜ - تم تغير اسم المجموعة 💘 ⋅\nمن قام بتغير الاسم » ⦗ {} ⦘ 💘 ⋅ ".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("-᚜ - » ⦗ أحتاج إلى صلاحية تعديل معلومات المجموعة ⦘ 💘 ⋅ ")

    else:
       await msg.edit("-᚜ - » ⦗ عليك الرد علي نص لوضعه اسم للمجموعه ⦘ 💘 ⋅ ")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command(["تغير الوصف", "تغير بايو الجروب"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("-᚜ - » ⦗ جاري تغير الوصف  ⦘ 💘 ⋅ ")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("- الامر دا للمجموعات بس  💘 ⋅ ")
    elif reply:
        try:
            discription = message.reply_to_message.text
            iLBaReD_Pin = await app.get_chat_member(chat_id, user_id)
            if iLBaReD_Pin.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("-᚜ - تم تغير وصف المجموعة 💘 ⋅\nمن قام بتغير الوصف » ⦗ {} ⦘ 💘 ⋅ ".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("- اعطيني صلاحة تعديل المجموعة لكي اقوم بتغير الوصف  💘 ⋅")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            iLBaReD_Pin = await app.get_chat_member(chat_id, user_id)
            if iLBaReD_Pin.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("-᚜ - تم تغير وصف المجموعة 💘 ⋅\nمن قام بتغير الوصف » ⦗ {} ⦘ 💘 ⋅ ".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("-᚜ - » ⦗ محتاج الي صلاحيات تعديل المجموعه ⦘ 💘 ⋅ ")
    else:
        
        await msg.edit("-᚜ - » ⦗ عليك الرد علي نص للتغير وصف المجموعه ⦘ 💘 ⋅ ")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["غادر", "عمر غادر"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "- حاضر هسمع الكلام باي ♥️😢 ⋅"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)
    await delete_served_chat(chat_id)


# --------------------------------------------------------------------------------- #

