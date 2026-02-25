import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from translation.languages import INDICTRANS_LANG_MAP, SUPPORTED_LANG_CODES

MODEL_NAME = "ai4bharat/indictrans2-en-indic-dist-200M"

print("[INFO] Loading IndicTrans2 model... This may take time on first run.")

# ----------------------------
# Load tokenizer & model
# ----------------------------
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True,
    torch_dtype=torch.float32
)

model.eval()


def translate_english(text: str, target_lang: str) -> str:
    """
    Translate English text into an Indian language (native script)
    """

    if target_lang not in SUPPORTED_LANG_CODES:
        raise ValueError(f"Unsupported language code: {target_lang}")

    src_tag = INDICTRANS_LANG_MAP["en"]
    tgt_tag = INDICTRANS_LANG_MAP[target_lang]

    input_text = f"{src_tag} {tgt_tag} {text}"

    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        truncation=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=256,
            num_beams=1,
            do_sample=False,
            use_cache=False
        )

    decoded = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True
    ).strip()

    return decoded