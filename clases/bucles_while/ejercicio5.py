import random

numero_secreto = random.randint(1, 100)
intento = int(input("Adivina el numero: "))

while intento != numero_secreto:
    if intento < numero_secreto:
        print("El numero es mayor")
    else:
        print("El numero es menor")

    intento = int(input("Intenta de nuevo: "))

print("Correcto, adivinaste el numero")