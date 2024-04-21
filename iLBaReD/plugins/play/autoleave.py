import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from iLBaReD import app
from iLBaReD.core.call import Omar, autoend
from iLBaReD.utils.database import get_client, is_active_chat, is_autoend


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        while not await asyncio.sleep(
            config.AUTO_LEAVE_ASSISTANT_TIME
        ):
            from iLBaReD.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.iter_dialogs():
                        chat_type = i.ChatType
                        if chat_type in [
                            SUPERGROUP,
                            GROUP ,
                            CHANNEL ,
                        ]:
                            chat_id = i.chat.id
                            if (
                                i.chat.id != config.LOGGER_ID
                                and i.chat.id != -1001517089988
                                and i.chat.id != -1001517089988
                            ):
                                if left == 20:
                                    continue
                                if not await is_active_chat(i.chat.id):
                                    try:
                                        await client.leave_chat(i.chat.id)
                                        left += 1
                                    except:
                                        continue
                except:
                    pass


asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        ender = await is_autoend()
        if not ender:
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Omar.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "تم انهاء التشغيل لعدم وجود مستمعين ♥️🌿",
                    )
                except:
                    continue


asyncio.create_task(auto_end())
                                       
