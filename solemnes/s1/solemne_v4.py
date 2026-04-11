# Solemne 1 V4 - Solucion Parte II
# Menu iterativo con opciones 1, 2 y 3

opcion = 0

while opcion != 4:
    print("--- MENu PRINCIPAL ---")
    print("1. Estacionamiento")
    print("2. Tienda")
    print("3. Transporte privado")
    print("4. Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        suma_horas = 0
        suma_pagos = 0
        cant_auto = 0
        cant_camioneta = 0
        cant_moto = 0

        for i in range(1, 11):
            print("Vehiculo", i)

            tipo = input("Tipo de vehiculo (automovil/camioneta/motocicleta): ")
            horas = float(input("Horas estacionadas: "))

            if tipo == "automovil":
                tarifa = 1200
                cant_auto += 1
            elif tipo == "camioneta":
                tarifa = 1500
                cant_camioneta += 1
            elif tipo == "motocicleta":
                tarifa = 800
                cant_moto += 1
            else:
                print("Tipo no valido. Se asumira motocicleta.")
                tarifa = 800
                cant_moto += 1

            pago = tarifa * horas

            if horas >= 3 and horas <= 5:
                descuento = pago * 0.05
            elif horas >= 6 and horas <= 8:
                descuento = pago * 0.10
            elif horas > 8:
                descuento = pago * 0.15
            else:
                descuento = 0

            pago_final = pago - descuento

            suma_horas += horas
            suma_pagos += pago_final

        promedio_horas = suma_horas / 10
        promedio_pago = suma_pagos / 10

        print("--- RESULTADOS ---")
        print("Promedio de horas estacionadas:", promedio_horas)
        print("Promedio de pago:", promedio_pago)
        print("Cantidad de automoviles:", cant_auto)
        print("Cantidad de camionetas:", cant_camioneta)
        print("Cantidad de motocicletas:", cant_moto)

    elif opcion == 2:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad: "))

        total_compra = precio * cantidad

        if total_compra > 200000:
            descuento = total_compra * 0.08
        elif total_compra > 100000:
            descuento = total_compra * 0.05
        else:
            descuento = 0

        total_pagar = total_compra - descuento

        print("--- RESULTADOS OPCION 2 ---")
        print("Total de la compra:", total_compra)
        print("Descuento aplicado:", descuento)
        print("Total a pagar:", total_pagar)

    elif opcion == 3:
        kilometros = float(input("Ingrese los kilometros recorridos: "))
        valor_km = float(input("Ingrese el valor por kilometro: "))

        pago_bruto = kilometros * valor_km

        if kilometros > 250:
            km_extra = kilometros - 250
            bono = (km_extra * valor_km) * 0.20
        else:
            bono = 0

        pago_bruto_total = pago_bruto + bono
        descuento_comision = pago_bruto_total * 0.10
        descuento_mantenimiento = pago_bruto_total * 0.05
        pago_liquido = pago_bruto_total - descuento_comision - descuento_mantenimiento

        print("--- RESULTADOS OPCION 3 ---")
        print("Pago bruto total:", pago_bruto_total)
        print("Descuento por comision:", descuento_comision)
        print("Descuento por mantenimiento:", descuento_mantenimiento)
        print("Pago liquido final:", pago_liquido)

    elif opcion == 4:
        print("Vuelva pronto.")

    else:
        print("Opcion no valida.")
