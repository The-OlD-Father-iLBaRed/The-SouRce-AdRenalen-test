import speech_recognition as sr
from pyrogram import Client, filters
from pydub import AudioSegment
from os import remove
from iLBaReD import app

@app.on_message(filters.regex("اكتب")& filters.group)
async def speech_to_text(client, message):
    if not message.reply_to_message:
        await message.reply("الرد على صوت.")
        return
    sent_message = await message.reply("جاري تحميل الصوت")
    voice_down = await message.reply_to_message.download("./recyad.wav")
    voice = sr.Recognizer()
    await sent_message.edit("جاري استخراج سورس الصوت")
    sound = AudioSegment.from_ogg(voice_down)
    wav_file = sound.export(voice_down, format="wav")
    with sr.AudioFile(wav_file) as source:
        audio_source = voice.record(source)
    await sent_message.edit("جاري التعرف علي الكلام")
    try:
        text = voice.recognize_google(audio_source, language= ar-EG )
    except Exception as e:
        text = f"فشل التعرف علي الكلام\n{e}"
    await message.reply(text)
    remove("recyad.wav")
async def is_heroku():
    return "heroku" in socket.getfqdn()
