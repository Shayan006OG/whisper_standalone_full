import os

# ---------- IMPORTS ----------
from stt_cli import main as whisper_cli_main
from translation.translator import translate_english
from tts.piper_tts import speak


# ---------- CONFIG ----------
AUDIO_PATH = "test_audio/sample1.m4a"
TARGET_LANG = "bn"   # hi, bn, ta, te, ml, kn, gu, pa, mr, or


def run_pipeline(audio_path: str, target_lang: str):
    print("\n================ PIPELINE START ================\n")

    # 1️⃣ SPEECH TO TEXT (WHISPER)
    print("🎙️ Step 1: Speech → Text (Whisper)")
    from stt_cli import transcribe_file
    english_text = transcribe_file(audio_path)

    print("\nENGLISH TRANSCRIPT:")
    print(english_text)

    # 2️⃣ TRANSLATION (IndicTrans2)
    print("\n🌐 Step 2: Translation (IndicTrans2)")
    translated_text = translate_english(english_text, target_lang)

    print(f"\n{target_lang.upper()} TRANSLATION:")
    print(translated_text)

    # 3️⃣ TEXT TO SPEECH (Piper)
    print("\n🔊 Step 3: Text → Speech (Piper)")
    output_file = f"tts/output/tts_{target_lang}.wav"
    speak(translated_text, output_file)

    print("\n================ PIPELINE END ==================")
    print(f"🎧 Audio saved at: {output_file}\n")


if __name__ == "__main__":
    run_pipeline(AUDIO_PATH, TARGET_LANG)
