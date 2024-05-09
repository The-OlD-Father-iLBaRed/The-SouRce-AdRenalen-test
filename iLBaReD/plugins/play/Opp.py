from iLBaReD import app
from pyrogram import enums
from pyrogram import Client
from strings.filters import command
import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

@app.on_message(command(["تخ","بيو"]))
async def Katl(client: Client, message: Message):
    if message.reply_to_message.from_user.id == 1924832439:
        await message.reply("لا يمكنك قتل مطور السورس ي غبي 😋♥️ ،")
    elif message.reply_to_message.from_user.id == message.from_user.id:
        await message.reply("لا يمكنك قتل نفسك")
    elif message.reply_to_message.from_user.id == app.id:
        await message.reply("لا يمكنك قتل البوت")
    else:
        # آيدي الشخص الذي عمل عليه رد الريبلي
        replied_user_id = message.reply_to_message.from_user.id
        replied_user_name = message.reply_to_message.from_user.first_name
        # آيدي الشخص الذي قام بإرسال رد الريبلي
        killer_id = message.from_user.id
        killer_name = message.from_user.first_name
        await message.reply_video(
            video=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
            caption=f"- القاتل المفتري » ⦗ {killer_name} (tg://user?id={killer_id}) ⦘\n- المقتول بمسدس مايه » ⦗ {replied_user_name} (tg://user?id={replied_user_id}) ⦘ \nانا لله وانا اليه راجعون الواد مات بمسدس لعبه 😂!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "- ضفني في جروبك يرايق 😋♥️ ،", url=f"https://t.me/{app.username}?startgroup=true"),
                    ],
                ]
            ),
            parse_mode=enums.ParseMode.MARKDOWN
        )

@app.on_message(command(["اصفخص","اتفو","تف"]))
async def Katl(client: Client, message: Message):
    if message.reply_to_message.from_user.id == 1924832439:
        await message.reply("مش هخليك تبوس مطوري عشان بغير 😂♥️ ،")
    elif message.reply_to_message.from_user.id == message.from_user.id:
        await message.reply("ايه الي وصلك لدرجة انك تتف علي نفسك 😋♥️ ،")
    elif message.reply_to_message.from_user.id == app.id:
        await message.reply("انتا عبيط يبني عايزني اتف علي نفسي 😋♥️ ،")
    else:
        # آيدي الشخص الذي عمل عليه رد الريبلي
        replied_user_id = message.reply_to_message.from_user.id
        replied_user_name = message.reply_to_message.from_user.first_name
        # آيدي الشخص الذي قام بإرسال رد الريبلي
        killer_id = message.from_user.id
        killer_name = message.from_user.first_name
        await message.reply_video(
            video=f"https://telegra.ph/file/53d48c7071f55d97a79cc.mp4",
        caption=f"- المنتن هذا » ⦗ [{killer_name}](tg://user?id={killer_id}) ⦘\n- تف في بق البني ادم دا » ⦗ [{replied_user_name}](tg://user?id={replied_user_id}) ⦘ \nاصفخص عليك عيل منتن 😂 ،",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "- ضفني في جروبك يرايق 😋♥️ ،", url=f"https://t.me/{app.username}?startgroup=true"),
                    ],
                ]
            ),
            parse_mode=enums.ParseMode.MARKDOWN
        )
@app.on_message(command(["اموه","مح","بوسه","بوثه"]))
async def Katl(client: Client, message: Message):
    if message.reply_to_message.from_user.id == 1924832439:
        await message.reply("مش هخليك تبوس مطوري عشان بغير 😂♥️ ،")
    elif message.reply_to_message.from_user.id == message.from_user.id:
        await message.reply("هيحح مش هينفع تبوس نفسك 😋♥️ ،")
    elif message.reply_to_message.from_user.id == app.id:
        await message.reply("مش هعرف ابوس نفسي والله 😋♥️ ،")
    else:
        # آيدي الشخص الذي عمل عليه رد الريبلي
        replied_user_id = message.reply_to_message.from_user.id
        replied_user_name = message.reply_to_message.from_user.first_name
        # آيدي الشخص الذي قام بإرسال رد الريبلي
        killer_id = message.from_user.id
        killer_name = message.from_user.first_name
        await message.reply_video(
            video=f"https://telegra.ph/file/53a81f2a11f10313a2337.mp4",
        caption=f"- المتحرش دا » ⦗ [{killer_name}](tg://user?id={killer_id}) ⦘\n- اتحرش بي الجسه دي » ⦗ [{replied_user_name}](tg://user?id={replied_user_id}) ⦘ \nمنكو لله ملبتو البلد ي انجاس 😂 ،",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "- ضفني في جروبك يرايق 😋♥️ ،", url=f"https://t.me/{app.username}?startgroup=true"),
                    ],
                ]
            ),
            parse_mode=enums.ParseMode.MARKDOWN
        )
        
