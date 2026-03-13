# Inicio del programa
print("EMPIEZA")

# Variables que cuentan los puntos seguidos de cada jugador
pts_seguidos_a = 1   # A empieza sacando, por eso parte con 1
pts_seguidos_b = 0   # B aún no tiene puntos seguidos

# Variables que almacenan el puntaje total de cada jugador
total_pts_a = 0
total_pts_b = 0

# Se indica que el saque inicial es de A
print(f"SACA A")

# Bucle infinito: se repite hasta que se cumpla la condición de término
while True:
    # Se espera el input del punto ganado: "A" o "B"
    punto = input()
    # Se actualiza quién ganó el punto y se resetean los puntos seguidos del rival
    if punto == "A":
        pts_seguidos_a += 1
        pts_seguidos_b = 0
    else:
        pts_seguidos_b += 1
        pts_seguidos_a = 0
    # Se muestra quién ganó el punto
    print(f"GANA {punto}")
    # Si A gana 2 puntos seguidos, suma un punto al total
    if pts_seguidos_a >= 2:
        total_pts_a += 1
    # Si B gana 2 puntos seguidos, suma un punto al total
    elif pts_seguidos_b >= 2:
        total_pts_b += 1
    # Se imprime el marcador actual
    print(f"A {total_pts_a} B {total_pts_b}")
    # Se calcula la diferencia de puntos
    diferencia = abs(total_pts_a - total_pts_b)
    # Condición de fin: alguien debe tener al menos 5 puntos y
    # además llevar 2 de diferencia
    if diferencia >= 2 and (total_pts_a >= 5 or total_pts_b >= 5):
        break
    # Se muestra quién saca en la siguiente jugada
    print(f"SACA {punto}")

print("FINAL")