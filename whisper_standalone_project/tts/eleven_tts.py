from elevenlabs.client import ElevenLabs
import os
import uuid

# 🔑 PUT YOUR API KEY HERE
API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
# "sk_487396871cc356036cf44ed68cc8828bea87da24928264d9"
client = ElevenLabs(api_key=API_KEY)

OUT_DIR = "tts/output"
os.makedirs(OUT_DIR, exist_ok=True)


def speak(text: str, lang: str = "hi"):
    """
    Generate natural neural speech using ElevenLabs
    """

    if not text.strip():
        return

    print("[ElevenLabs] Generating natural voice...")

    audio = client.text_to_speech.convert(
        text=text,
        voice_id="EXAVITQu4vr4xnSDxMaL",   # Rachel voice (natural)
        model_id="eleven_multilingual_v2"
    )

    file_path = os.path.join(
        OUT_DIR,
        f"eleven_{uuid.uuid4().hex}.mp3"
    )

    with open(file_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    print(f"[ElevenLabs] Audio saved → {file_path}")

    # auto play
    os.system(f'start "" "{file_path}"')