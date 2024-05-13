import asyncio
import random
from pyrogram import filters, Client
from pyrogram.types import Message
from iLBaReD import app
import config


txt = [
    "- اسرع واحد يدز الكلمة ~ ( بارده)",
    "- اسرع واحد يدز الكلمة ~ ( اجيت)",
    "**- اسرع واحد يدز الكلمة*ذ ~ ( جبان)",
    "- اسرع واحد يدز الكلمة ~ ( مافهمت)",
    "- اسرع واحد يدز الكلمة ~ ( ميت)",
]
correct_answers = [
    "بارده",
    "اجيت",
    "جبان",
    "مافهمت",
    "ميت",
]

current_question_index = 0

@app.on_message(filters.command(["كلمه"], ""))
async def game_handler(client: Client, message: Message):
    global current_question_index

    if current_question_index >= len(correct_answers):
        await message.reply("تم انتهاء الأسئلة.")
        return

    correct_answer = correct_answers[current_question_index]

    if message.text.lower() == correct_answer.lower():
        await message.reply("إجابة صحيحة!")
        current_question_index += 1

        if current_question_index < len(correct_answers):
            await message.reply(f"السؤال الحالي: {correct_answers[current_question_index]}")
        else:
            await message.reply("تم انتهاء الأسئلة. شكرًا للمشاركة.")
    else:
        await message.reply("إجابة خاطئة. حاول مرة أخرى.")
