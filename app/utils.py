# app/utils.py
import re

GOLD_FACTS = [
    "Gold has historically acted as a hedge against inflation.",
    "Digital gold lets you buy even very small quantities securely.",
    "Adding gold can reduce overall portfolio volatility."
]

YES_WORDS = {"yes", "haan", "ha", "yup", "ok", "okay", "proceed", "buy", "purchase", "sure"}
NO_WORDS  = {"no", "nahi", "nah", "later", "skip", "cancel"}

GOLD_PATTERNS = [
    r"\bgold\b", r"\bdigital gold\b", r"\bbuy gold\b",
    r"\binvest(ing|ment)? in gold\b", r"\bgold etf\b", r"\bsgb\b"
]

def text_has_any(text: str, words: set[str]) -> bool:
    t = text.lower()
    return any(re.search(rf"\b{re.escape(w)}\b", t) for w in words)

def is_gold_query(text: str) -> bool:
    t = text.lower()
    return any(re.search(p, t) for p in GOLD_PATTERNS)

def parse_grams(text: str):
    m = re.search(r"(\d+(\.\d+)?)\s*(g|gram|grams)?", text.lower())
    if m:
        try:
            return float(m.group(1))
        except:
            return None
    return None
