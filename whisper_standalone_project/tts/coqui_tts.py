from TTS.api import TTS
import torch
import os
import uuid

OUT_DIR = "tts/output"
os.makedirs(OUT_DIR, exist_ok=True)

# 🔹 Change model depending on language later
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"

print("[INFO] Loading Coqui TTS model...")

tts = TTS(MODEL_NAME)

def speak(text: str):
    if not text.strip():
        return

    out_file = os.path.join(
        OUT_DIR,
        f"coqui_{uuid.uuid4().hex}.wav"
    )

    tts.tts_to_file(
        text=text,
        file_path=out_file
    )

    print(f"[TTS] Audio saved → {out_file}")
    os.system(f'start "" "{out_file}"')