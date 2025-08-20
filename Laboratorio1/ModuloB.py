#------------------------------
#  B.1  Validación de entrada
#------------------------------
print("B.1  Validación de entrada")

def parsear_enteros(entradas: list[str]) -> tuple[list[int], list[str]]:
    valores = []
    errores = []
    for e in entradas:
        try:
            valores.append(int(e))
        except ValueError:
            errores.append(f"No se pudo convertir '{e}' a entero.")
    return valores, errores

entradas = ["10", "x", "3"]
valores, errores = parsear_enteros(entradas)
print("Valores:", valores)  
print("Errores:", errores)  


#------------------------------------
#  B.2  Excepciones personalizadas
#------------------------------------
print("B.2  Excepciones personalizadas")


class CantidadInvalida(Exception):
    pass

def calcular_total(precio_unitario, cantidad):
    if cantidad <= 0:
        raise CantidadInvalida("La cantidad debe ser mayor que cero.")
    if precio_unitario < 0:
        raise ValueError("El precio unitario no puede ser negativo.")
    return precio_unitario * cantidad

# Manejo de excepciones
try:
    print(calcular_total(10, 3)) 
    print(calcular_total(10, 0))  
except CantidadInvalida as e:
    print(f"Error de cantidad: {e}")
except ValueError as e:
    print(f"Error de valor: {e}")

