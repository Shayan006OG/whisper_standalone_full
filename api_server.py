from fastapi import FastAPI, UploadFile, File
import shutil
import os
import uuid

import whisper
from whisper_standalone_project.translation.translator import translate_english
from whisper_standalone_project.tts.eleven_tts import speak

app = FastAPI()

print("Loading Whisper model...")
whisper_model = whisper.load_model("medium")


@app.get("/")
def home():
    return {"message": "AI Translator API running"}


@app.post("/translate")
async def translate_audio(
    file: UploadFile = File(...),
    target_lang: str = "hi"
):
    """
    Upload audio → get translation + speech
    """

    temp_filename = f"temp_{uuid.uuid4().hex}.mp3"

    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 🔹 Whisper STT
    result = whisper_model.transcribe(temp_filename, fp16=False, language="en")
    english_text = result["text"].strip()

    # 🔹 Translate
    translated = translate_english(english_text, target_lang)

    # 🔹 TTS generate
    speak(translated, target_lang)

    os.remove(temp_filename)

    return {
        "english_text": english_text,
        "translated_text": translated,
        "language": target_lang
    }