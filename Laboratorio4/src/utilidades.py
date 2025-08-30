# src/utilidades.py

def contar_vocales(texto: str) -> int:
    """Cuenta las vocales en una cadena. Retorna 0 si está vacía."""
    if not isinstance(texto, str):
        raise TypeError("El argumento debe ser un string")
    return sum(1 for c in texto.lower() if c in "aeiou")

def es_par(n: int) -> bool:
    """Devuelve True si el número es par, False si es impar."""
    if not isinstance(n, int):
        raise TypeError("El argumento debe ser un entero")
    return n % 2 == 0

def dividir(a: float, b: float) -> float:
    """Divide dos números, lanza ZeroDivisionError si b == 0."""
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    return a / b
