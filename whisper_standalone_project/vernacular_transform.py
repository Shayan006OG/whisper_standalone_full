import re

# ----------------- Helpers ----------------- #

def _normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def _apply_replacements(text: str, mapping: dict) -> str:
    if not mapping:
        return text

    def repl(match):
        word = match.group(0)
        lower = word.lower()
        mapped = mapping.get(lower, word)
        if word.istitle():
            return mapped.capitalize()
        elif word.isupper():
            return mapped.upper()
        return mapped

    pattern = r"\b(" + "|".join(re.escape(k) for k in mapping.keys()) + r")\b"
    return re.sub(pattern, repl, text, flags=re.IGNORECASE)

# =========================================================
# ======================= HINGLISH ========================
# =========================================================

HINGLISH_PHRASES = {
    r"\bthis is\b": "yeh",
    r"\bi am\b": "main",
    r"\bwe are\b": "hum",
    r"\bvery good\b": "bahut achha",
    r"\bvery bad\b": "bahut kharab",
    r"\bno problem\b": "koi baat nahi",
    r"\bthank you\b": "shukriya",
    r"\blet us\b": "chalo",
    r"\bdo not worry\b": "tension mat lo",
}

HINGLISH_MAP = {
    "very": "bahut",
    "really": "kaafi",
    "friend": "yaar",
    "friends": "yaar log",
    "bro": "bhai",
    "brother": "bhai",
    "awesome": "mast",
    "great": "badhiya",
    "good": "achha",
    "cool": "mast",
    "problem": "issue",
    "work": "kaam",
    "working": "kaam kar raha",
    "project": "project",
    "time": "time",
    "today": "aaj",
    "yes": "haan",
    "no": "nahi",
    "okay": "theek hai",
    "what": "kya",
    "why": "kyun",
    "how": "kaise",
}

def to_hinglish(text):
    text = _normalize_spaces(text)
    for p, r in HINGLISH_PHRASES.items():
        text = re.sub(p, r, text, flags=re.IGNORECASE)
    text = _apply_replacements(text, HINGLISH_MAP)
    if len(text.split()) <= 12 and not text.lower().endswith("yaar"):
        text += " yaar"
    return text

# =========================================================
# ======================= BENGALI =========================
# =========================================================

BENGALI_PHRASES = {
    r"\bthis is\b": "eta",
    r"\bi am\b": "ami",
    r"\bvery good\b": "onek bhalo",
    r"\bvery bad\b": "onek kharap",
    r"\bno problem\b": "kono shomossha nei",
    r"\bthank you\b": "dhonnobad",
    r"\bdo not worry\b": "chinta korona",
}

BENGALI_MAP = {
    "very": "onek",
    "good": "bhalo",
    "bad": "kharap",
    "friend": "bondhu",
    "friends": "bondhura",
    "work": "kaaj",
    "working": "kaaj korchhi",
    "project": "project ta",
    "today": "aaj",
    "now": "ekhon",
    "problem": "shomossha",
    "easy": "shoja",
    "important": "khub important",
    "yes": "haan",
    "no": "na",
}

def to_bengali(text):
    text = _normalize_spaces(text)
    for p, r in BENGALI_PHRASES.items():
        text = re.sub(p, r, text, flags=re.IGNORECASE)
    text = _apply_replacements(text, BENGALI_MAP)
    if not text.lower().endswith("na"):
        text += " na"
    return text

# =========================================================
# ======================= PUNJABI =========================
# =========================================================

PUNJABI_PHRASES = {
    r"\bthis is\b": "eh",
    r"\bvery good\b": "bahut vadhiya",
    r"\bno problem\b": "koi gall nahi",
    r"\bthank you\b": "dhanyavaad ji",
}

PUNJABI_MAP = {
    "friend": "veere",
    "friends": "veere log",
    "bro": "veer",
    "brother": "veer ji",
    "very": "bahut",
    "good": "vadhiya",
    "great": "shandar",
    "work": "kaam",
    "project": "project",
    "yes": "haan ji",
    "no": "nahi ji",
}

def to_punjabi(text):
    text = _normalize_spaces(text)
    for p, r in PUNJABI_PHRASES.items():
        text = re.sub(p, r, text, flags=re.IGNORECASE)
    text = _apply_replacements(text, PUNJABI_MAP)
    if not text.lower().endswith("ji"):
        text += " ji"
    return text

# =========================================================
# ======================= TAMILISH ========================
# =========================================================

TAMILISH_PHRASES = {
    r"\bthis is\b": "idhu",
    r"\bi am\b": "naan",
    r"\bvery good\b": "romba nalla",
    r"\bno problem\b": "onnum illa",
    r"\bthank you\b": "nandri",
}

TAMILISH_MAP = {
    "what": "enna",
    "why": "yen",
    "how": "epdi",
    "friend": "machan",
    "friends": "machans",
    "good": "nalla",
    "bad": "mosam",
    "very": "romba",
    "problem": "kashtam",
    "work": "vela",
    "working": "vela panren",
    "project": "project",
    "today": "innaiku",
    "yes": "seri da",
    "no": "illa",
}

def to_tamilish(text):
    text = _normalize_spaces(text)
    for p, r in TAMILISH_PHRASES.items():
        text = re.sub(p, r, text, flags=re.IGNORECASE)
    text = _apply_replacements(text, TAMILISH_MAP)
    if not text.lower().endswith("da"):
        text += " da"
    return text

# =========================================================
# ======================= TELUGUISH =======================
# =========================================================

TELUGU_PHRASES = {
    r"\bthis is\b": "idi",
    r"\bvery good\b": "chaala bagundi",
    r"\bno problem\b": "em ledu",
    r"\bthank you\b": "dhanyavaadalu",
}

TELUGU_MAP = {
    "what": "emi",
    "why": "enduku",
    "how": "ela",
    "friend": "ra",
    "friends": "raalu",
    "good": "bagundi",
    "very": "chaala",
    "problem": "samasyya",
    "work": "pani",
    "project": "project",
    "yes": "avunu",
    "no": "ledu",
}

def to_teluguish(text):
    text = _normalize_spaces(text)
    for p, r in TELUGU_PHRASES.items():
        text = re.sub(p, r, text, flags=re.IGNORECASE)
    text = _apply_replacements(text, TELUGU_MAP)
    if not text.lower().endswith("ra"):
        text += " ra"
    return text

# =========================================================
# =================== MALAYALAMISH ========================
# =========================================================

MALAYALAM_PHRASES = {
    r"\bthis is\b": "ithu",
    r"\bvery good\b": "valare nallatha",
    r"\bno problem\b": "prashnam illa",
    r"\bthank you\b": "nanni",
}

MALAYALAM_MAP = {
    "what": "entha",
    "why": "enthina",
    "how": "engane",
    "friend": "machane",
    "good": "nallatha",
    "very": "valare",
    "problem": "prashnam",
    "work": "pani",
    "project": "project",
    "yes": "aah",
    "no": "illa",
}

def to_malayalamish(text):
    text = _normalize_spaces(text)
    for p, r in MALAYALAM_PHRASES.items():
        text = re.sub(p, r, text, flags=re.IGNORECASE)
    text = _apply_replacements(text, MALAYALAM_MAP)
    if not text.lower().endswith("da"):
        text += " da"
    return text

# =========================================================
# ======================= KANNADAISH ======================
# =========================================================

KANNADA_PHRASES = {
    r"\bthis is\b": "idu",
    r"\bvery good\b": "thumba chennagide",
    r"\bno problem\b": "samasyeyilla",
    r"\bthank you\b": "dhanyavaadagalu",
}

KANNADA_MAP = {
    "what": "enu",
    "why": "yaake",
    "how": "hege",
    "friend": "maga",
    "good": "chennagide",
    "very": "thumba",
    "problem": "samasye",
    "work": "kelasa",
    "project": "project",
    "yes": "howdu",
    "no": "illa",
}

def to_kannadaish(text):
    text = _normalize_spaces(text)
    for p, r in KANNADA_PHRASES.items():
        text = re.sub(p, r, text, flags=re.IGNORECASE)
    text = _apply_replacements(text, KANNADA_MAP)
    if not text.lower().endswith("maga"):
        text += " maga"
    return text

# =========================================================
# ======================= GUJARATIISH =====================
# =========================================================

GUJARATI_PHRASES = {
    r"\bthis is\b": "aa",
    r"\bi am\b": "hu",
    r"\bwe are\b": "ame",
    r"\bvery good\b": "ghanu saru",
    r"\bvery bad\b": "ghanu kharab",
    r"\bnot good\b": "saru nathi",
    r"\bno problem\b": "koi vandho nathi",
    r"\bthank you\b": "aabhar",
    r"\bplease\b": "krupaya",
    r"\bdo not worry\b": "chinta na karo",
    r"\blet us\b": "chalo",
}

GUJARATI_MAP = {
    # basics
    "what": "shu",
    "why": "kem",
    "how": "kevrite",
    "when": "kyare",
    "where": "kya",

    # people
    "friend": "yaar",
    "friends": "yaaro",
    "bro": "bhai",
    "brother": "bhai",
    "people": "loko",

    # quality / emotion
    "good": "saru",
    "bad": "kharap",
    "great": "jordar",
    "awesome": "jordar",
    "very": "ghanu",
    "easy": "saral",
    "difficult": "mushkel",
    "important": "important che",

    # work / study
    "work": "kaam",
    "working": "kaam kari rahyo",
    "project": "project",
    "college": "college",
    "study": "abhyas",
    "exam": "exam",

    # time
    "today": "aaje",
    "now": "have",
    "time": "samay",

    # responses
    "yes": "haan",
    "no": "nathi",
    "okay": "barabar",
    "ok": "barabar",

    # problems
    "problem": "vandho",
    "problems": "vandha",

    # actions
    "come": "aavo",
    "go": "jao",
    "doing": "kari rahyo",
}

def to_gujaratiish(text: str) -> str:
    text = _normalize_spaces(text)

    # phrase-level first
    for p, r in GUJARATI_PHRASES.items():
        text = re.sub(p, r, text, flags=re.IGNORECASE)

    # word-level
    text = _apply_replacements(text, GUJARATI_MAP)

    # Gujarati sentence ending
    if not text.lower().endswith(("che", ".", "!", "?")):
        text += " che"

    return text

# =========================================================
# ======================= MARWARIISH ======================
# =========================================================

MARWARI_PHRASES = {
    r"\bthis is\b": "aa",
    r"\bvery good\b": "ghani bhali",
    r"\bno problem\b": "koi baat koni",
    r"\bthank you\b": "ram ram sa",
}

MARWARI_MAP = {
    "friend": "bhaya",
    "good": "bhali",
    "very": "ghani",
    "problem": "dikhat",
    "work": "kaam",
    "project": "project",
    "yes": "haan sa",
    "no": "naa sa",
}

def to_marwariish(text):
    text = _normalize_spaces(text)
    for p, r in MARWARI_PHRASES.items():
        text = re.sub(p, r, text, flags=re.IGNORECASE)
    text = _apply_replacements(text, MARWARI_MAP)
    if not text.lower().endswith("sa"):
        text += " sa"
    return text

# =========================================================
# ======================= BHOJPURI ========================
# =========================================================

BHOJPURI_PHRASES = {
    r"\bthis is\b": "ee",
    r"\bi am\b": "hum",
    r"\bvery good\b": "bahut badhiya",
    r"\bvery bad\b": "bahut kharab",
    r"\bno problem\b": "koi dikkat nahi",
    r"\bthank you\b": "dhanyavaad",
    r"\bdo not worry\b": "chinta mat kara",
}

BHOJPURI_MAP = {
    "friend": "bhaiya",
    "friends": "bhaiya log",
    "bro": "babu",
    "brother": "bhaiya",
    "good": "badhiya",
    "very": "bahut",
    "problem": "dikhat",
    "work": "kaam",
    "working": "kaam karat ba",
    "project": "project",
    "today": "aaj",
    "now": "abhi",
    "yes": "haan",
    "no": "na",
    "what": "ka",
    "why": "kahe",
    "how": "kaise",
}

def to_bhojpuri(text: str) -> str:
    text = _normalize_spaces(text)
    for p, r in BHOJPURI_PHRASES.items():
        text = re.sub(p, r, text, flags=re.IGNORECASE)
    text = _apply_replacements(text, BHOJPURI_MAP)
    if not text.lower().endswith(("ba", ".", "!", "?")):
        text += " ba"
    return text


# =========================================================
# =================== MASTER CONTROL ======================
# =========================================================

SUPPORTED_MODES = {
    "none": "No transformation",
    "hinglish": "Hindi-English (Hinglish)",
    "bengali": "Bengali-flavoured English",
    "punjabi": "Punjabi-flavoured English",
    "tamilish": "Tamil-flavoured English",
    "teluguish": "Telugu-flavoured English",
    "malayalamish": "Malayalam-flavoured English",
    "kannadaish": "Kannada-flavoured English",
    "gujaratiish": "Gujarati-flavoured English",
    "marwariish": "Rajasthani / Marwari style English",
    "bhojpuri": "Bhojpuri / Bihari-flavoured English",
}

def transform(text: str, mode: str = "none") -> str:
    text = _normalize_spaces(text)
    mode = (mode or "none").lower()

    if mode == "hinglish":
        return to_hinglish(text)
    if mode == "bengali":
        return to_bengali(text)
    if mode == "punjabi":
        return to_punjabi(text)
    if mode == "tamilish":
        return to_tamilish(text)
    if mode == "teluguish":
        return to_teluguish(text)
    if mode == "malayalamish":
        return to_malayalamish(text)
    if mode == "kannadaish":
        return to_kannadaish(text)
    if mode == "gujaratiish":
        return to_gujaratiish(text)
    if mode == "marwariish":
        return to_marwariish(text)
    if mode == "bhojpuri":
        return to_bhojpuri(text)

    return text