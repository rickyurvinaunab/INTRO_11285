# Escribe tu código aquí :D
cant_reposo_maxima = 0
cant_maxima_reposo = 0
edad = int(input())
fcm = 220 - edad
actual = ""
anterior = ""
while True:
    frecuencia = int(input())
    porcentaje = frecuencia/fcm*100
    anterior = actual
    if frecuencia == -1:
        break
    if porcentaje<=55:#Reposo
        actual = "reposo"
    elif porcentaje>=95:# Máxima:
        actual = "maxima"
    else:
        actual = ""
    if anterior == "reposo" and actual == "maxima":
        cant_reposo_maxima += 1
    if anterior == "maxima" and actual == "reposo":
        cant_maxima_reposo += 1
print("Reposo a Maxima:", cant_reposo_maxima)
print("Maxima a Reposo:", cant_maxima_reposo)