# Escribe tu código aquí
from metro import primera, proxima

def cuan_lejos(linea, estacion_1, estacion_2):
    contador = 0
    if estacion_1 == estacion_2:
        return 0
    while True:
        prox = proxima(linea, estacion_1)
        contador += 1
        if prox == estacion_2:
            return contador
        estacion_1 = prox
        if prox == "":
            return -1

    return -1