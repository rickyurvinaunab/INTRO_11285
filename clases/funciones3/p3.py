from hotel import num_habitaciones as nh
from hotel import  nombre_ocupante as no
from hotel import  obtener_caracter as oc

def se_puede_excursion(cantidad):
    cant_timi = 0
    cant_extro = 0
    for hab in range(nh()):
        perro = no(hab)
        caracter = oc(perro)
        if caracter == "timido":
            cant_timi += 1
        else:
            cant_extro += 1
    nece_timi = cant_timi / 5
    cant_bus_timi = int(nece_timi)
    # print("cant_bus_timi", cant_bus_timi)
    if nece_timi %1 >0 :
        cant_bus_timi += 1
    nece_extro = cant_extro / 5
    cant_bus_extro = int(nece_extro)
    # print("cant_bus_extro", cant_bus_extro)

    if nece_extro %1 >0 :
        cant_bus_extro += 1
    necesidad_total = cant_bus_timi + cant_bus_extro
    if cantidad < necesidad_total:
        print(f"Insuficientes: se tienen {cantidad} y se necesitan {necesidad_total}")
    else:
        print(f"Suficientes: se tienen {cantidad} y se necesitan {necesidad_total}")




