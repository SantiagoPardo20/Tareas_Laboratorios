# src/validador_csv.py
import csv
from pathlib import Path

def leer_csv(ruta: str) -> list[dict[str, str]]:
    """Lee un CSV y devuelve una lista de diccionarios."""
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        return list(lector)
