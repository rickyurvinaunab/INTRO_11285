envio = input("Envio la tarea (si/no): ")

if envio == "no":
    print("Sin entrega")
else:
    hora = int(input("Ingrese hora de entrega: "))

    if hora >= 14 and hora <= 20:
        print("Entrega valida")
    else:
        print("Entrega fuera de plazo")
