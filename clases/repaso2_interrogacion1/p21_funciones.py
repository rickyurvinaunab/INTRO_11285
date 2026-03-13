from djs import digito, largo

# Solicita dos numeros de entrada
num1 = int(input())
num2 = int(input())

# Contador de numeros que cumplen la condicion (introescos)
cant_introescos = 0

# Recorre todos los numeros entre num1 y num2 (incluido num2)
for num in range(num1, num2+1):
    # Calcula la cantidad de digitos del numero
    largo_num = largo(num)
    # Inicializa los contadores de digitos requeridos
    cant_uno = 2   # se necesitan al menos 2 digitos "1"
    cant_tres = 1  # se necesita al menos 1 digito "3"
    cant_cero = 1  # se necesita al menos 1 digito "0"

    # Si el numero tiene menos de 3 digitos, no cumple y se pasa al siguiente
    if largo_num < 3:
        continue

    # Recorre cada posicion del numero
    for i in range(largo_num):
        # Obtiene el digito en la posicion i
        dig = digito(num, i)
        # Resta a los contadores segun el digito encontrado
        if dig == 1:
            cant_uno -= 1
        elif dig == 0:
            cant_cero -= 1
        elif dig == 3:
            cant_tres -= 1

        # Si ya se cumplieron todos los requisitos de digitos
        if cant_uno <= 0 and cant_cero <= 0 and cant_tres <= 0:
            # Se cuenta el numero como introesco
            cant_introescos += 1
            # Se imprime el numero que cumple
            print(num)
            # Se sale del ciclo para no seguir revisando mas digitos
            break

# Al finalizar, imprime la cantidad total de numeros que cumplen la condicion
print(cant_introescos)