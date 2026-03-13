# Funcion que define el criterio de ordenamiento
def criterio(item):
    return item[1], item[2], item[3], item[4], item[5]

# Funcion que ordena una lista de vuelos y retorna los primeros k
def ordenar_vuelos(vuelos_desordenados, k):
    vuelos_cancelados = []      # Lista para guardar los vuelos cancelados
    vuelos_no_cancelados = []   # Lista para guardar los vuelos no cancelados
    # Separa los vuelos segun si estan cancelados o no
    for vuelo in vuelos_desordenados:
        if vuelo[6] == 'Cancelado':
            vuelos_cancelados.append(vuelo)
        else:
            vuelos_no_cancelados.append(vuelo)
    # Ordena ambos grupos usando el criterio definido
    vuelos_cancelados.sort(key=criterio)
    vuelos_no_cancelados.sort(key=criterio)
    # Junta primero los cancelados y luego los no cancelados
    vuelos_cancelados.extend(vuelos_no_cancelados)
    # Retorna solo los primeros k vuelos de la lista final
    return vuelos_cancelados[:k]