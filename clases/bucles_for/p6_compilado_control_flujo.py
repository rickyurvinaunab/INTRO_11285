cantidad = int(input())
cant_brach = 0
cant_tita = 0
cant_brach_seguidos = 0
cant_tita_seguidos = 0
for i in range(cantidad):
    fosil = int(input())
    if fosil == 1:
        # si recibo un fosil == 1
        # aumento la cantidad de brach seguidos en 1
        cant_brach_seguidos += 1
        cant_tita_seguidos = 0
        if cant_brach_seguidos == 2:
            # si la cant de brach seguidos es 2 
            # significa que forme un Brachiosaurus
            cant_brach += 1
            # aumento en 1 la cantidad de Brachiosaurus
            cant_brach_seguidos = 0
            # reinicio el contador
    elif fosil == 2:
        cant_tita_seguidos += 1
        cant_brach_seguidos = 0
        if cant_tita_seguidos == 3:
            cant_tita += 1
            cant_tita_seguidos = 0
    else:
        # si no recibo 1 o 2 reinicio los contadores
        cant_brach_seguidos = 0
        cant_tita_seguidos = 0
print(f"Brachiosaurus: {cant_brach}")
print(f"Titanosaurus: {cant_tita}")