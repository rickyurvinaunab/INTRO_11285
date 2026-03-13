import hotel

def revisar_asignacion():
    contador = 0
    for hab1 in range(hotel.num_habitaciones()):
        nombre = hotel.nombre_ocupante(hab1)
        for hab2 in range(hab1+1, hotel.num_habitaciones()):
            nombre2 = hotel.nombre_ocupante(hab2)
            if nombre == nombre2:
                contador += 1
    return contador


