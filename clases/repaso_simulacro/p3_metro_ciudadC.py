# Escribe tu código aquí

from metro import nombre, numero, primera, proxima

linea1 = input()
linea2 = input()
cant_est_1 = numero(linea1)
cant_est_2 = numero(linea2)

for n_est_l1 in range(1, cant_est_1+1):
    nombre1 = nombre(linea1, n_est_l1)
    for n_est_l2 in range(1, cant_est_2+1):
        nombre2 = nombre(linea2, n_est_l2)
        if nombre1 == nombre2:
            print(nombre1)