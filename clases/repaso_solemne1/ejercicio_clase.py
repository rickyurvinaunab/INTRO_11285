opcion = 0
while opcion != 4:
    print("\nMENU PRINCIPAL")
    print("1. Control de peso de cajas")
    print("2. Analisis de compras")
    print("3. Analisis de notas")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        i = 1
        menores_10 = 0
        entre_10_20 = 0
        mayores_20 = 0
        suma_pesos = 0
        while i <= 8:
            peso = float(input("Ingrese el peso de la caja: "))
            suma_pesos = suma_pesos + peso
            if peso < 10:
                menores_10 += 1
            elif peso <= 20:
                entre_10_20 += 1
            else:
                mayores_20 += 1
            i += 1
        promedio = suma_pesos / 8
        print("Cajas < 10 kg:", menores_10)
        print("Cajas entre 10 y 20 kg:", entre_10_20)
        print("Cajas > 20 kg:", mayores_20)
        print("Promedio de peso:", promedio)
    elif opcion == 2:
        i = 1
        mas_10_productos = 0
        mas_50000 = 0
        suma_gasto = 0
        mayor_compra = 0
        while i <= 6:
            productos = int(input("Ingrese cantidad de productos: "))
            monto = float(input("Ingrese monto de compra: "))
            suma_gasto += monto
            if productos > 10:
                mas_10_productos += 1
            if monto > 50000:
                mas_50000 += 1
            if i == 1 or monto > mayor_compra:
                mayor_compra = monto
            i += 1
        promedio = suma_gasto / 6
        print("Clientes con más de 10 productos:", mas_10_productos)
        print("Clientes que gastaron más de 50000:", mas_50000)
        print("Promedio de gasto:", promedio)
        print("Mayor compra:", mayor_compra)

    elif opcion == 3:
        i = 1
        aprobados = 0
        reprobados = 0
        suma_notas = 0
        while i <= 10:
            nota = float(input("Ingrese nota: "))
            suma_notas += nota
            if nota >= 4.0:
                aprobados += 1
            else:
                reprobados += 1
            if i == 1:
                mayor = nota
                menor = nota
            else:
                if nota > mayor:
                    mayor = nota
                if nota < menor:
                    menor = nota
            i += 1
        promedio = suma_notas / 10
        print("Aprobados:", aprobados)
        print("Reprobados:", reprobados)
        print("Promedio:", promedio)
        print("Nota mayor:", mayor)
        print("Nota menor:", menor)
    elif opcion == 4:
        print("Vuelva pronto")
    else:
        print("Opcion invalida")