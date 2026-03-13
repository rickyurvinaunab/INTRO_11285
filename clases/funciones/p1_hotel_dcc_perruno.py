# Escribe tu código aquí
from hotel import num_habitaciones, nombre_ocupante

def obtener_habitacion(nombre):
    n_habitaciones = num_habitaciones()
    #llamo a la funcion que retorna el
    # num de habitaciones y eso almaceno en
    # n_habitaciones
    for i in range(n_habitaciones):
        # recorrdo cada habitacion, el # de habitaciones
        # es la variable i -> int
        ocupante = nombre_ocupante(i)
        # busco el ocupante de esa habitacion con la
        # funcion nombre ocupante, el nombre del ocupante
        # lo almaceno en ocupante
        if ocupante == nombre:
            # comparo si el ocupante es = al nombre
            # del perro que recibir como paramentro
            # y retorno i que corresponde a la habitacion
            return i

    # si acabe de recorrer todas las habitaciones
    # y no encontre el nombre retorno -1
    return -1