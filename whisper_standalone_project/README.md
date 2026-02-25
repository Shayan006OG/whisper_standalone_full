# Whisper Standalone Speech-to-Text (STT) Tools

This project provides command-line tools to experiment with Whisper:
- Transcribe existing audio files
- Record from microphone and transcribe
- Chunked "real-time" streaming transcription
- Accuracy evaluation using Word Error Rate (WER)

## 1. Setup

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On Linux/Mac

pip install -r requirements.txt
```

## 2. Transcribe an audio file

```bash
python stt_cli.py path/to/audio_file.wav
```

## 3. Record from microphone and transcribe

```bash
python mic_record.py my_voice.wav 5
python stt_cli.py my_voice.wav
```

## 4. Chunked streaming-style transcription

```bash
python stream_whisper.py
```

Speak into the mic. It prints partial transcripts every few seconds.
Press Ctrl+C to stop.

## 5. Accuracy Evaluation (WER)

1. Put test audio files into `test_audio/`
2. Create `test_set.csv` like:

```csv
file,transcript
sample1.wav,good morning how are you
sample2.wav,this project is about vernacular translation
```

3. Run:

```bash
python eval_accuracy.py
```

This prints Word Error Rate (WER) over the dataset.
