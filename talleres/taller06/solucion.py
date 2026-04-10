opcion = 0

while opcion != 4:
    print("MENU PRINCIPAL")
    print("1. Calorias quemadas en gimnasio")
    print("2. Analisis de ventas")
    print("3. Proceso de seleccion")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        i = 1
        menos_200 = 0
        entre_200_500 = 0
        mas_500 = 0
        suma_calorias = 0
        while i <= 7:
            calorias = float(input("Ingrese la cantidad de calorias quemadas: "))
            suma_calorias = suma_calorias + calorias
            if calorias < 200:
                menos_200 = menos_200 + 1
            elif calorias <= 500:
                entre_200_500 = entre_200_500 + 1
            else:
                mas_500 = mas_500 + 1
            i = i + 1
        promedio = suma_calorias / 7
        print("Personas que quemaron menos de 200 calorias:", menos_200)
        print("Personas que quemaron entre 200 y 500 calorias:", entre_200_500)
        print("Personas que quemaron mas de 500 calorias:", mas_500)
        print("Promedio de calorias quemadas:", promedio)
    elif opcion == 2:
        i = 1
        menores_100000 = 0
        mayores_300000 = 0
        total_ventas = 0
        mayor_venta = 0
        dia_mayor = 0
        while i <= 5:
            venta = float(input("Ingrese el monto vendido del dia: "))
            total_ventas = total_ventas + venta
            if venta < 100000:
                menores_100000 = menores_100000 + 1
            if venta > 300000:
                mayores_300000 = mayores_300000 + 1
            if i == 1 or venta > mayor_venta:
                mayor_venta = venta
                dia_mayor = i
            i = i + 1
        print("Dias con ventas menores a $100000:", menores_100000)
        print("Dias con ventas mayores a $300000:", mayores_300000)
        print("Total acumulado de ventas:", total_ventas)
        print("El dia con mayor venta fue el dia:", dia_mayor)
        print("Monto de la mayor venta:", mayor_venta)
    elif opcion == 3:
        i = 1
        aprobados = 0
        rechazados = 0
        suma_puntajes = 0
        while i <= 6:
            puntaje = float(input("Ingrese el puntaje del postulante: "))
            suma_puntajes = suma_puntajes + puntaje
            if puntaje >= 70:
                aprobados = aprobados + 1
            else:
                rechazados = rechazados + 1
            if i == 1:
                mayor = puntaje
                menor = puntaje
            else:
                if puntaje > mayor:
                    mayor = puntaje
                if puntaje < menor:
                    menor = puntaje
            i = i + 1
        promedio = suma_puntajes / 6
        print("Postulantes aprobados:", aprobados)
        print("Postulantes rechazados:", rechazados)
        print("Puntaje promedio:", promedio)
        print("Puntaje mas alto:", mayor)
        print("Puntaje mas bajo:", menor)
    elif opcion == 4:
        print("Programa finalizado. Gracias por utilizar el sistema.")
    else:
        print("Opcion invalida. Intente nuevamente.")