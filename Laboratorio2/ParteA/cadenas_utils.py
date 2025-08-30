#--------------------------------------------
#Utilidades de cadenas
#--------------------------------------------

import re
import unicodedata

__all__ = ["normalize", "is_valid_slug", "format_title", "require_non_empty"]

_SMALL_WORDS = {"a", "al", "del", "de", "la", "las", "el", "los", "y", "o", "u", "en", "con", "para"}


def _strip_accents(s: str) -> str:
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def normalize(texto: str) -> str:
    if not isinstance(texto, str):
        raise TypeError("normalize espera un str")
    texto = texto.strip()
    texto = _strip_accents(texto).lower()
    texto = re.sub(r"\s+", " ", texto)
    return texto


def is_valid_slug(texto: str) -> bool:
    if not isinstance(texto, str):
        return False
    if " " in texto:
        return False
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", texto))


def format_title(texto: str) -> str:
    if not isinstance(texto, str):
        raise TypeError("format_title espera un str")
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


def require_non_empty(texto: str) -> str:
    if not isinstance(texto, str):
        raise TypeError("require_non_empty espera un str")
    if not texto.strip():
        raise ValueError("El texto no puede estar vacío")
    return texto
