

























# Ejercicio 1: Cuenta Ascendente 
# Escribe un programa que utilice un bucle while para contar de 1 a 10 e 
# imprima cada número. 

# n = 1
# while n < 11:
#     print(n)
#     n = n + 1
#     # n += 1





# Ejercicio 2: Suma de Números 
# Escribe un programa que pida al usuario un número y utilice un bucle 
# while para sumar todos los números desde 1 hasta el número ingresado. 

# n = int(input())
# aux = 1
# suma = 0
# while n+1 > aux:
#     suma = suma + aux
#     aux += 1

# print(suma)





# Ejercicio 3: Promedio de Notas 
# Escribe un programa que permita al usuario ingresar un número 
# desconocido de notas, calcular su promedio, y finalizar la entrada cuando el
#  usuario ingrese una nota negativa.

nota = float(input())
promedio = 0
suma = 0
contador = 0
while nota >=0:
    suma = suma + nota
    print("suma", suma)
    contador += 1
    print("contador", contador)
    nota = float(input())

if contador > 0:
    promedio = suma / contador

print("promedio", promedio)

