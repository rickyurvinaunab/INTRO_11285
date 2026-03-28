tipo_pasajero = input("Ingrese tipo de pasajero (economica o ejecutiva): ")
peso_maleta = float(input("Ingrese peso de la maleta: "))

if tipo_pasajero == "economica":
    if peso_maleta <= 23:
        print("Puede pasar sin costo extra")
    else:
        print("Debe pagar sobrepeso")
elif tipo_pasajero == "ejecutiva":
    if peso_maleta <= 32:
        print("Puede pasar sin costo extra")
    else:
        print("Debe pagar sobrepeso")
else:
    print("Tipo de pasajero invalido")
