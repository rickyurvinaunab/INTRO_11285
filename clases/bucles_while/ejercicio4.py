n = int(input("Ingrese un numero: "))

factorial = 1
contador = 1

while contador <= n:
    factorial = factorial * contador
    contador += 1

print("El factorial es:", factorial)