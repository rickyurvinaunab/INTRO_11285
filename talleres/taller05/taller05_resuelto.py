
continuar_menu = "si"

while continuar_menu == "si":
    print("==============================")
    print("          MENU")
    print("==============================")
    print("1. Arriendo de departamentos")
    print("2. Calculo de interes bancario")
    print("3. Calculo de pintura para un cuarto")
    print("4. Salir")
    print("==============================")

    opcion = input("Ingrese una opcion (1, 2, 3 o 4): ")

    # --------------------------------------------------
    # OPCION 1: Arriendo de departamentos
    # --------------------------------------------------
    if opcion == "1":
        print("--- ARRIENDO DE DEPARTAMENTOS ---")

        cantidad_clientes = int(input("Ingrese la cantidad de clientes: "))

        # Acumuladores y contadores para los calculos finales
        contador = 1
        total_dias = 0
        total_monto_final = 0

        cantidad_1_habitacion = 0
        cantidad_2_habitaciones = 0
        cantidad_3_habitaciones = 0

        while contador <= cantidad_clientes:
            print("Departamento arrendado N: ", contador)

            nombre_arrendatario = input("Ingrese el nombre del arrendatario: ")
            rut_arrendador = input("Ingrese el rut del arrendador: ")
            habitaciones = int(input("Ingrese la cantidad de habitaciones (1, 2 o 3): "))
            dias = int(input("Ingrese la cantidad de dias de arriendo: "))

            # Determinar precio diario segun cantidad de habitaciones
            if habitaciones == 1:
                precio_diario = 30000
                cantidad_1_habitacion = cantidad_1_habitacion + 1
            elif habitaciones == 2:
                precio_diario = 45000
                cantidad_2_habitaciones = cantidad_2_habitaciones + 1
            elif habitaciones == 3:
                precio_diario = 55000
                cantidad_3_habitaciones = cantidad_3_habitaciones + 1
            else:
                # Si el usuario ingresa un valor incorrecto, se asume 1 habitacion
                print("Cantidad de habitaciones no valida. Se considerara 1 habitacion.")
                precio_diario = 30000
                cantidad_1_habitacion = cantidad_1_habitacion + 1

            monto_bruto = precio_diario * dias

            # Si arrienda por mas de 7 dias, obtiene descuento
            if dias > 7:
                descuento = monto_bruto * 0.085
            else:
                descuento = 0

            monto_final = monto_bruto - descuento

            # Acumular para promedios
            total_dias = total_dias + dias
            total_monto_final = total_monto_final + monto_final

            # Mostrar resumen por cada departamento arrendado
            print("Resumen del arriendo:")
            print("Nombre del arrendatario:", nombre_arrendatario)
            print("Rut del arrendador:", rut_arrendador)
            print("Monto bruto a pagar: $", round(monto_bruto, 2))
            print("Descuento: $", round(descuento, 2))
            print("Monto final a pagar: $", round(monto_final, 2))

            contador = contador + 1

        # Calculo de promedios
        if cantidad_clientes > 0:
            promedio_dias = total_dias / cantidad_clientes
            promedio_monto_final = total_monto_final / cantidad_clientes
        else:
            promedio_dias = 0
            promedio_monto_final = 0

        # Mostrar resultados finales
        print("========== RESUMEN GENERAL ==========")
        print("Cantidad de departamentos arrendados:", cantidad_clientes)
        print("Promedio de dias de arriendo:", round(promedio_dias, 2))
        print("Promedio de monto final:", round(promedio_monto_final, 2))
        print("Cantidad de departamentos de 1 habitacion:", cantidad_1_habitacion)
        print("Cantidad de departamentos de 2 habitaciones:", cantidad_2_habitaciones)
        print("Cantidad de departamentos de 3 habitaciones:", cantidad_3_habitaciones)

    # --------------------------------------------------
    # OPCION 2: Calculo de interes bancario
    # --------------------------------------------------
    elif opcion == "2":
        print("--- CALCULO DE INTERES BANCARIO ---")

        capital = float(input("Ingrese el capital: "))
        tiempo = int(input("Ingrese el tiempo en meses: "))

        # La tasa es 2%, por eso se usa 0.02
        tasa = 0.02

        monto_interes = capital * tasa * tiempo
        capital_total = capital + monto_interes

        print("Resultados:")
        print("Monto de interes: $", round(monto_interes, 2))
        print("Capital total: $", round(capital_total, 2))

    # --------------------------------------------------
    # OPCION 3: Calculo de pintura para un cuarto
    # --------------------------------------------------
    elif opcion == "3":
        print("--- CALCULO DE PINTURA PARA UN CUARTO ---")

        # Se ingresan las medidas de las 4 paredes
        area_total = 0
        for i in range(1, 5):
            ancho = float(input(f"Ingrese el ancho de la pared {i} en metros: "))
            alto = float(input(f"Ingrese el alto de la pared {i} en metros: "))
            area = ancho * alto
            area_total = area_total + area
        # Medidas de la puerta
        ancho_puerta = float(input("Ingrese el ancho de la puerta en metros: "))
        alto_puerta = float(input("Ingrese el alto de la puerta en metros: "))

        area_puerta = ancho_puerta * alto_puerta
        area_a_pintar = area_total - area_puerta

        # Un litro cubre 3 metros cuadrados
        litros_pintura = area_a_pintar / 3

        print("Resultados:")
        print("Area total de las paredes:", round(area_total, 2), "m2")
        print("Area de la puerta:", round(area_puerta, 2), "m2")
        print("Area total a pintar:", round(area_a_pintar, 2), "m2")
        print("Litros de pintura necesarios:", round(litros_pintura, 2), "litros")

    # --------------------------------------------------
    # OPCION 4: Salir
    # --------------------------------------------------
    elif opcion == "4":
        continuar_menu = "no"
        print("Vuelva pronto.")

    # --------------------------------------------------
    # Opcion invalida
    # --------------------------------------------------
    else:
        print("Opcion no valida. Intente nuevamente.")

    # Si no eligio salir, preguntar si desea volver al menu
    if continuar_menu == "si":
        respuesta = input("Desea volver al menu? (si/no): ")

        if respuesta != "si":
            continuar_menu = "no"
            print("Vuelva pronto.")
