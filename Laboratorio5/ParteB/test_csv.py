# test_csv.py
import pytest
from validador_csv import leer_csv

@pytest.fixture
def dataset():
    return leer_csv("Lottery_Powerball_Winning_Numbers__Beginning_2010.csv")

def test_columnas_obligatorias(dataset):
    columnas = dataset[0].keys()
    assert "Draw Date" in columnas
    assert "Winning Numbers" in columnas
    assert "Multiplier" in columnas

def test_no_filas_vacias(dataset):
    assert len(dataset) > 0, "El dataset no debe estar vacío"

def test_formato_fecha(dataset):
    for fila in dataset:
        fecha = fila["Draw Date"]
        assert fecha.count("/") == 2, f"Fecha inválida: {fecha}"

def test_winning_numbers_tienen_6(dataset):
    for fila in dataset:
        numeros = fila["Winning Numbers"].split()
        assert len(numeros) == 6, f"Fila con cantidad incorrecta de números: {numeros}"

def test_numeros_son_enteros(dataset):
    for fila in dataset:
        numeros = fila["Winning Numbers"].split()
        for n in numeros:
            assert n.isdigit(), f"Número inválido: {n}"

def test_multiplier_es_entero_o_vacio(dataset):
    for fila in dataset:
        mult = fila["Multiplier"].strip()
        # Permitimos vacío (sin multiplicador)
        if mult != "":
            assert mult.isdigit(), f"Multiplier inválido: {mult}"

def test_multiplier_valores_validos(dataset):
    valores_validos = [2, 3, 4, 5, 10]
    for fila in dataset:
        mult = fila["Multiplier"].strip()
        if mult != "":
            mult = int(mult)
            assert mult in valores_validos, f"Multiplier fuera de rango: {mult}"
