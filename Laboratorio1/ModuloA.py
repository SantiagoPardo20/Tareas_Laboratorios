#----------------------------------
#A.1  Funciones como valores
#----------------------------------
print("A.1  Funciones como valores") 

def saludar(nombre):
    return f"Hola, {nombre}"

def despedir(nombre):
    return f"Adiós, {nombre}"

def aplaudir(nombre):
    return f"Bravo Bravo Bravo, {nombre}!"

acciones = {
    "saludar": saludar,
    "despedir": despedir,
    "aplaudir": aplaudir
}

# Función para ejecutar una acción por su nombre
def ejecutar(accion, *args, **kwargs):
    if accion not in acciones:
        raise ValueError(f"Acción '{accion}' no existe.")
    return acciones[accion](*args, **kwargs)

print(ejecutar("saludar", "Ana"))  
print(ejecutar("aplaudir", "Luis")) 


#---------------------------------------
# A.2  Funciones internas y closures
#---------------------------------------
print("A.2  Funciones internas y closures")

def crear_descuento(porcentaje):
    def aplicar_descuento(precio):
        return precio * (1 - porcentaje)
    return aplicar_descuento  # Closure

descuento10 = crear_descuento(0.10)
descuento25 = crear_descuento(0.25)

print(descuento10(100))  # 90.0
print(descuento25(80))   # 60.0

