# Solemne 1 V5 - Solucion Parte II
# Menu iterativo con opciones 1, 2 y 3

opcion = 0

while opcion != 4:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Biblioteca")
    print("2. Consumo de internet")
    print("3. Cibercafe")
    print("4. Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        suma_dias = 0
        suma_pagos = 0
        cant_infantil = 0
        cant_novela = 0
        cant_academico = 0

        for i in range(1, 11):
            print("\nPrestamo", i)

            categoria = input("Categoria del libro (infantil/novela/academico): ")
            dias = int(input("Cantidad de dias de prestamo: "))

            if categoria == "infantil":
                tarifa = 1000
                cant_infantil += 1
            elif categoria == "novela":
                tarifa = 1500
                cant_novela += 1
            elif categoria == "academico":
                tarifa = 2000
                cant_academico += 1
            else:
                print("Categoria no valida. Se asumira infantil.")
                tarifa = 1000
                cant_infantil += 1

            pago = tarifa

            if dias >= 3 and dias <= 5:
                recargo = pago * 0.05
            elif dias >= 6 and dias <= 10:
                recargo = pago * 0.08
            elif dias > 10:
                recargo = pago * 0.12
            else:
                recargo = 0

            total = pago + recargo

            suma_dias += dias
            suma_pagos += total

        promedio_dias = suma_dias / 10
        promedio_pago = suma_pagos / 10

        print("\n--- RESULTADOS OPCION 1 ---")
        print("Promedio de dias de prestamo:", promedio_dias)
        print("Promedio de pago:", promedio_pago)
        print("Cantidad de libros infantil:", cant_infantil)
        print("Cantidad de libros novela:", cant_novela)
        print("Cantidad de libros academico:", cant_academico)

    elif opcion == 2:
        gb = float(input("Ingrese la cantidad de GB consumidos: "))
        consumo = gb * 350

        if gb > 100:
            recargo = consumo * 0.10
        elif gb > 50:
            recargo = consumo * 0.05
        else:
            recargo = 0

        total_pagar = consumo + recargo

        print("\n--- RESULTADOS OPCION 2 ---")
        print("Consumo:", consumo)
        print("Recargo:", recargo)
        print("Total a pagar:", total_pagar)

    elif opcion == 3:
        horas = float(input("Ingrese la cantidad de horas de uso: "))
        valor_hora = float(input("Ingrese el valor por hora: "))

        costo_base = horas * valor_hora

        if horas > 5:
            recargo = costo_base * 0.10
        else:
            recargo = 0

        total_pagar = costo_base + recargo

        print("\n--- RESULTADOS OPCION 3 ---")
        print("Costo base:", costo_base)
        print("Monto del recargo:", recargo)
        print("Total a pagar:", total_pagar)

    elif opcion == 4:
        print("Vuelva pronto.")

    else:
        print("Opcion no valida.")
