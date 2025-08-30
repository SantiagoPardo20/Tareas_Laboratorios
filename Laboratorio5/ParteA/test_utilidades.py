# test_utilidades.py
import pytest
from utilidades import contar_vocales, es_primo, invertir_fecha

# --- contar_vocales ---
def test_contar_vocales_correcto():
    assert contar_vocales("Hola") == 2
    assert contar_vocales("Python") == 1

def test_contar_vocales_vacio():
    assert contar_vocales("") == 0

def test_contar_vocales_tipo_invalido():
    with pytest.raises(TypeError):
        contar_vocales(123)

# --- es_primo ---
def test_es_primo_correcto():
    assert es_primo(2)
    assert es_primo(7)
    assert not es_primo(9)

def test_es_primo_cero_uno():
    assert not es_primo(0)
    assert not es_primo(1)

def test_es_primo_tipo_invalido():
    with pytest.raises(TypeError):
        es_primo("texto")

# --- invertir_fecha ---
def test_invertir_fecha_correcto():
    assert invertir_fecha("2024-12-31") == "31/12/2024"

def test_invertir_fecha_formato_invalido():
    with pytest.raises(ValueError):
        invertir_fecha("31-12-2024")  # Formato incorrecto

def test_invertir_fecha_tipo_invalido():
    with pytest.raises(ValueError):
        invertir_fecha(None)  # No es cadena

