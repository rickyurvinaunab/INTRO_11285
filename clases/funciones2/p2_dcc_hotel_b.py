from hotel import num_habitaciones, nombre_ocupante

def revisar_asignacion():
    contador = 0
    n_habitaciones = num_habitaciones()
    for i in range(n_habitaciones):
        nombre = nombre_ocupante(i)
        for j in range(i+1, n_habitaciones):
            nombre2 = nombre_ocupante(j)
            if nombre == nombre2:
                contador += 1
    return contador