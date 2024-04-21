import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(
    command(["صورتي","صوري"])
    & filters.group
    & ~filters.edited
)
async ah madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""غير صورتك بقا قرفتنا 😏""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],[
                    InlineKeyboardButton(
                        "╞. 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 .╡", url=f"https://t.me/so_alfaa"),
                ],
            ]
        ),
    )
