# Se inicializa la variable que acumula la suma de los números positivos
suma = 0
# Se pide el primer número al usuario
num = int(input())
# El ciclo se repite mientras el número no sea 0
while num != 0:
    # Caso 1: si el número es negativo
    if num < 0:
        # La cantidad de números que NO se sumarán corresponde al valor absoluto del número negativo
        cant = abs(num)
        print(f"NO SUMA {num}")
        # Mientras queden "cant" números por saltarse
        while cant != 0:
            num = int(input())
            # Si el usuario ingresa 0, se rompe inmediatamente
            if num == 0:
                break
            # Se muestra que este número tampoco se suma
            print(f"NO SUMA {num}")
            # Si también es negativo, se descuenta en la cuenta de "castigos"
            if num < 0:
                cant -= 1
    # Caso 2: si el número es positivo
    else:
        # Se suma al acumulado
        suma += num
        print(f"SI SUMA {num}")
    # Si en algún momento el número es 0, se termina el bucle principal
    if num == 0:
        break
    # Se pide el siguiente número para continuar el ciclo
    num = int(input())
# Al salir del bucle se imprime el mensaje final y el resultado de la suma
print("FIN")
print(suma)