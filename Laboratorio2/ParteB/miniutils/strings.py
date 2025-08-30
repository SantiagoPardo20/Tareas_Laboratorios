import re
import unicodedata

__all__ = ["normalize", "is_valid_slug", "format_title", "collapse_spaces"]

_SMALL_WORDS = {"a", "al", "del", "de", "la", "las", "el", "los", "y", "o", "u", "en", "con", "para"}


def collapse_spaces(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _strip_accents(s: str) -> str:
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def normalize(texto: str) -> str:
    if not isinstance(texto, str):
        raise TypeError("normalize espera un str")
    texto = collapse_spaces(texto)
    texto = _strip_accents(texto).lower()
    return texto


def is_valid_slug(texto: str) -> bool:
    if not isinstance(texto, str) or " " in texto:
        return False
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", texto))


def format_title(texto: str) -> str:
    texto = normalize(texto)
    palabras = texto.split(" ")
    if not palabras:
        return ""
    res = []
    for i, w in enumerate(palabras):
        if 0 < i < len(palabras) - 1 and w in _SMALL_WORDS:
            res.append(w)
        else:
            res.append(w.capitalize())
    return " ".join(res)
