# tests/test_validador_csv.py
from src.validador_csv import leer_csv

def test_columnas_presentes(tmp_path):
    # Crear CSV temporal
    data = "id,nombre,edad\n1,Ana,23\n2,Carlos,30\n"
    archivo = tmp_path / "test.csv"
    archivo.write_text(data, encoding="utf-8")

    filas = leer_csv(str(archivo))
    assert all(col in filas[0] for col in ["id", "nombre", "edad"])

def test_tipos_validos(tmp_path):
    data = "id,nombre,edad\n1,Ana,23\n2,Carlos,30\n"
    archivo = tmp_path / "test.csv"
    archivo.write_text(data, encoding="utf-8")

    filas = leer_csv(str(archivo))
    for fila in filas:
        assert int(fila["id"]) > 0
        assert isinstance(fila["nombre"], str)
        assert int(fila["edad"]) >= 0

def test_ids_unicos(tmp_path):
    data = "id,nombre,edad\n1,Ana,23\n1,Otro,40\n"
    archivo = tmp_path / "test.csv"
    archivo.write_text(data, encoding="utf-8")

    filas = leer_csv(str(archivo))
    ids = [fila["id"] for fila in filas]
    assert len(ids) == len(set(ids)), "Los IDs deben ser únicos"
