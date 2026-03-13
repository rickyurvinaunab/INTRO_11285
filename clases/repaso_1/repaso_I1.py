

tiempo_max = 0
nombre_ganador = ""
for i in range(3):
    numero = int(input())
    nombre = input()
    if numero > tiempo_max:
        tiempo_max = numero
        nombre_ganador = nombre
print("El ganador es: ", nombre_ganador)

