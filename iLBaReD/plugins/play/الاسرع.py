import asyncio
import random
from pyrogram import filters, Client
from pyrogram.types import Message
from iLBaReD import app
import config

questions = [
    "- اسرع واحد يدز الكلمة ~ ( بارده)",
    "- اسرع واحد يدز الكلمة ~ ( اجيت)",
    "- اسرع واحد يدز الكلمة ~ ( جبان)",
    "- اسرع واحد يدز الكلمة ~ ( مافهمت)",
    "- اسرع واحد يدز الكلمة ~ ( ميت)",
]

answers = [
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

    if current_question_index >= len(questions):
        await message.reply("تم انتهاء الأسئلة.")
        return

    current_question = questions[current_question_index]
    correct_answer = answers[current_question_index]

        if current_question_index < len(questions):
            await message.reply(f"السؤال الحالي: {questions[current_question_index]}")
        else:
            await message.reply("تم انتهاء الأسئلة. شكرًا للمشاركة.")
    else:
        await message.reply("إجابة خاطئة. حاول مرة أخرى.")

        # إرسال سؤال جديد عند الإجابة الخاطئة
        if current_question_index < len(questions):
            await message.reply(f"السؤال الحالي: {questions[current_question_index]}")
