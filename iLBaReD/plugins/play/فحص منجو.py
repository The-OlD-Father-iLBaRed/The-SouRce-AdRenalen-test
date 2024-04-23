from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from iLBaReD  import app 
mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')


@app.on_message(filters.command(["فحص المونجو","فحص"],""))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("- استخدم الامر مثل ⦗ فحص + mongodb ⦘")
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("- كود المنجو دا شغال تقدر تستخدمو ✨♥️ ،")
        except Exception as e:
            await message.reply(f"- فشل الاتصال السبب : {e}")
    else:
        await message.reply("- الكود دا مش شغال مينفعش تستخدمو ✨♥️ ،")
