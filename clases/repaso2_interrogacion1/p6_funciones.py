# Importa funciones del modulo hotel
from hotel import num_habitaciones, nombre_ocupante, obtener_caracter

def se_puede_excursion(cantidad):
    # Obtiene el numero total de habitaciones
    cant_hab = num_habitaciones()
    # Contadores para extrovertidos e introvertidos
    cant_extro = 0
    cant_intro = 0
    cantidad_necesaria = 0
    # Recorre cada habitacion del hotel
    for hab in range(cant_hab):
        # Obtiene el nombre del ocupante de la habitacion
        perro = nombre_ocupante(hab)
        # Obtiene el caracter del ocupante (extrovertido o introvertido)
        caracter = obtener_caracter(perro)
        # Suma al contador segun el tipo de caracter
        if caracter == "extrovertido":
            cant_extro += 1
        else:
            cant_intro += 1
    # Calcula la cantidad de buses necesarios para los extrovertidos (1 por cada 5)
    total_extro = -(-cant_extro // 5)
    # Calcula la cantidad de buses necesarios para los introvertidos (1 por cada 5)
    total_intro = -(-cant_intro // 5)
    # Cantidad total de buses necesarios
    cantidad_necesaria = total_extro + total_intro
    # Compara si la cantidad entregada es suficiente
    if cantidad_necesaria <= cantidad:
        print(f"Suficientes: se tienen {cantidad} y se necesitan {cantidad_necesaria}")
    else:
        print(f"Insuficientes: se tienen {cantidad} y se necesitan {cantidad_necesaria}")