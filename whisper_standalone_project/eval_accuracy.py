import csv
import os
import whisper
from jiwer import wer, RemovePunctuation, ToLowerCase, Strip, Compose

TEST_AUDIO_DIR = "test_audio"
TEST_CSV = "test_set.csv"

# Text normalization (VERY important for fair evaluation)
transform = Compose([
    ToLowerCase(),
    RemovePunctuation(),
    Strip()
])

def load_test_set(csv_path):
    files = []
    refs = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            files.append(row["file"])
            refs.append(row["transcript"])
    return files, refs

def main():
    print("[INFO] Loading Whisper model (medium for better accuracy)...")
    model = whisper.load_model("medium")

    files, refs = load_test_set(TEST_CSV)
    preds = []

    print("\n============= PER FILE EVALUATION =============\n")

    for fname, ref in zip(files, refs):
        path = os.path.join(TEST_AUDIO_DIR, fname)
        print(f"[INFO] Transcribing {path}")

        result = model.transcribe(path, fp16=False)
        hyp = result.get("text", "")

        # Normalize texts
        ref_norm = transform(ref)
        hyp_norm = transform(hyp)

        preds.append(hyp_norm)

        file_wer = wer(ref_norm, hyp_norm)
        file_acc = (1 - file_wer) * 100

        print("REF :", ref)
        print("HYP :", hyp.strip())
        print(f"WER : {file_wer:.3f}")
        print(f"ACC : {file_acc:.2f}%")
        print("-" * 50)

    # Overall metrics
    overall_wer = wer(
        [transform(r) for r in refs],
        preds
    )
    overall_acc = (1 - overall_wer) * 100

    print("\n================ OVERALL REPORT ================")
    print(f"Overall WER      : {overall_wer:.3f}")
    print(f"Overall Accuracy : {overall_acc:.2f}%")
    print("================================================")

if __name__ == "__main__":
    main()
