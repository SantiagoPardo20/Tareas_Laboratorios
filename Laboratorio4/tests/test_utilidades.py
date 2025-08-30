# tests/test_utilidades.py
import pytest
from src.utilidades import contar_vocales, es_par, dividir

def test_contar_vocales_normal():
    assert contar_vocales("Hola Mundo") == 4

def test_contar_vocales_vacio():
    assert contar_vocales("") == 0

def test_contar_vocales_error_tipo():
    with pytest.raises(TypeError):
        contar_vocales(123)

def test_es_par_casos():
    assert es_par(2) is True
    assert es_par(3) is False

def test_es_par_error_tipo():
    with pytest.raises(TypeError):
        es_par(2.5)

def test_dividir_valido():
    assert dividir(10, 2) == 5

def test_dividir_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
