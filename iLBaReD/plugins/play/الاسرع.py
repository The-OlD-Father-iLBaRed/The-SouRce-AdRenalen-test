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

current_question_index = None

@app.on_message(filters.command(["كلمه"], ""))
async def game_start(client: Client, message: Message):
    global current_question_index

    current_question_index = random.randint(0, len(questions) - 1)
    current_question = questions[current_question_index]

    await message.reply(current_question)

@app.on_message(filters.text & ~filters.me)
async def check_answer(client: Client, message: Message):
    global current_question_index

    if current_question_index is None:
        return

    correct_answer = answers[current_question_index]

    if message.text.lower() == correct_answer:
        await message.reply("إجابة صحيحة!")
        current_question_index = None
    else:
        await message.reply("إجابة خاطئة. حاول مرة أخرى.")
