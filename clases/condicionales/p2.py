edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad <= 12:
    print("Nino")
elif edad >= 13 and edad <= 19:
    print("Adolescente")
elif edad >= 20 and edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad invalida")