clima = input()
salon_disponible = input()
asistentes = int(input())
presupuesto = int(input())

lugar_evento = "cancelado"

if clima == "soleado":
    if asistentes > 100 and presupuesto > 2000000:
        lugar_evento = "Parque Bicentenario"
    elif asistentes <= 100:
        lugar_evento = "seccion pequena del parque"
    elif presupuesto <= 2000000:
        if salon_disponible == "si":
            lugar_evento = "salon cerrado"
        else:
            lugar_evento = "cancelado"

elif clima == "nublado":
    if salon_disponible == "si":
        if presupuesto >= 2000000:
            lugar_evento = "salon cerrado"
        else:
            lugar_evento = "salon cerrado con servicios reducidos"
    else:
        if asistentes < 50:
            lugar_evento = "seccion pequena del parque"
        else:
            lugar_evento = "cancelado"

elif clima == "lluvia":
    if salon_disponible == "si":
        lugar_evento = "salon cerrado"
    else:
        lugar_evento = "cancelado"

print("El evento se realizara en:", lugar_evento)