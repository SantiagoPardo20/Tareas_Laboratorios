# validador_csv.py
import csv
from typing import List, Dict

def leer_csv(ruta: str) -> List[Dict[str, str]]:
    """
    Lee un archivo CSV y retorna una lista de diccionarios.
    Cada fila tiene las claves: 'Draw Date', 'Winning Numbers', 'Multiplier'
    """
    with open(ruta, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
