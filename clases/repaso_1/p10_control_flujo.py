cantidad_tickets = 0
cantidad_entran = 0
while True:
    ticket = input()
    cantidad_a_entrar = int(ticket[-2:])
    cantidad_tickets += 1
    cantidad_entran += cantidad_a_entrar
    cantidad_permitida = 100 - cantidad_entran
    if cantidad_permitida < 0:
        quedaron_fuera = cantidad_permitida * -1
        entraron = cantidad_a_entrar - quedaron_fuera
        print(f"{entraron} entraron y {quedaron_fuera} quedaron fuera con el ticket {ticket}")
        if cantidad_tickets >= 10:
            print("No leo mas tickets y se lleno.")
            break
        print("No cabe mas gente. No se salte la reja por favor.")
        break
    else:
        print(f"{cantidad_a_entrar} entraron con el ticket {ticket}")
        if cantidad_tickets == 10:
            print("No leo mas tickets.")
            break