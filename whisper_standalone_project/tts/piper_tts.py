import subprocess
import os
import uuid
import unicodedata
import re

# ----------------------------
# Piper Configuration
# ----------------------------
PIPER_EXE = "tts/piper/piper.exe"
OUT_DIR = "tts/output"

os.makedirs(OUT_DIR, exist_ok=True)

# ----------------------------
# Language → Model Mapping
# (EDIT paths according to your downloaded models)
# ----------------------------
LANG_MODELS = {
    "en": "tts/models/en_US-lessac-medium.onnx",
    "hi": "tts/models/hi_IN-pratham-medium.onnx",   # Hindi
    "bn": "tts/models/bn_IN.onnx",   # Bengali
    "ta": "tts/models/ta_IN.onnx",   # Tamil
    "te": "tts/models/te_IN.onnx",   # Telugu
    "mr": "tts/models/mr_IN.onnx",   # Marathi
    "gu": "tts/models/gu_IN.onnx",   # Gujarati
    "kn": "tts/models/kn_IN.onnx",   # Kannada
    "ml": "tts/models/ml_IN.onnx",   # Malayalam
    "pa": "tts/models/pa_IN.onnx",   # Punjabi
}

# Fallback model (if language not found)
DEFAULT_MODEL = LANG_MODELS["en"]


# ----------------------------
# Unicode-Safe Sanitizer (CRITICAL)
# Keeps Indic scripts intact
# ----------------------------
def _sanitize_text(text: str) -> str:
    if not text:
        return ""

    # Normalize Unicode properly (keeps Hindi/Bengali/Tamil etc.)
    text = unicodedata.normalize("NFC", text)

    # Remove control characters only (NOT language characters)
    text = re.sub(r"[\x00-\x1F\x7F]", "", text)

    # Clean extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ----------------------------
# Get model based on language
# ----------------------------
def _get_model(lang: str) -> str:
    model = LANG_MODELS.get(lang)

    if model and os.path.exists(model):
        return model

    print(f"[TTS WARNING] Model for '{lang}' not found. Using fallback English model.")
    return DEFAULT_MODEL


# ----------------------------
# Main Speak Function (Multilingual)
# ----------------------------
def speak(text: str, lang: str = "en", output_path: str | None = None):
    """
    Multilingual TTS using Piper.
    Accepts native script (Hindi, Bengali, Tamil, etc.)
    NO romanization needed.
    """

    if not text or not text.strip():
        print("[TTS WARNING] Empty text received")
        return

    safe_text = _sanitize_text(text)

    if not safe_text:
        print("[TTS WARNING] Text empty after sanitization")
        return

    model_path = _get_model(lang)

    # Generate output file
    if output_path:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        out_file = output_path
    else:
        out_file = os.path.join(
            OUT_DIR,
            f"tts_{lang}_{uuid.uuid4().hex}.wav"
        )

    cmd = [
        PIPER_EXE,
        "--model", model_path,
        "--output_file", out_file
    ]

    try:
        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8"
        )

        # Send native script text directly (VERY IMPORTANT)
        process.stdin.write(safe_text)
        process.stdin.close()
        process.wait()

        if os.path.exists(out_file):
            print(f"[TTS] ({lang}) Audio saved → {out_file}")
            os.system(f'start "" "{out_file}"')
        else:
            print("[TTS ERROR] WAV file not generated")

    except Exception as e:
        print("[TTS EXCEPTION]", e)