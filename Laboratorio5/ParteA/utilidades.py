# utilidades.py

def contar_vocales(cadena: str) -> int:
    """
    Cuenta el número de vocales en una cadena.
    Parámetros:
        cadena (str): texto de entrada
    Retorna:
        int: número de vocales
    """
    if not isinstance(cadena, str):
        raise TypeError("La entrada debe ser una cadena")
    return sum(1 for c in cadena.lower() if c in "aeiou")


def es_primo(n: int) -> bool:
    """
    Verifica si un número es primo.
    Parámetros:
        n (int): número a verificar
    Retorna:
        bool: True si es primo, False en caso contrario
    """
    if not isinstance(n, int):
        raise TypeError("La entrada debe ser un entero")
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def invertir_fecha(fecha: str) -> str:
    """
    Invierte el formato de fecha de 'YYYY-MM-DD' a 'DD/MM/YYYY'.
    """
    if not isinstance(fecha, str):
        raise ValueError("La fecha debe ser una cadena en formato YYYY-MM-DD")

    partes = fecha.split("-")
    if len(partes) != 3:
        raise ValueError("Formato de fecha incorrecto, esperado YYYY-MM-DD")

    yyyy, mm, dd = partes

    # Validaciones básicas
    if len(yyyy) != 4 or len(mm) != 2 or len(dd) != 2:
        raise ValueError("Formato de fecha incorrecto, esperado YYYY-MM-DD")

    return f"{dd}/{mm}/{yyyy}"
