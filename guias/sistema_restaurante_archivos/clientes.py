from utilidades import leer_menu, agregar_cliente, agregar_pedido, leer_pedidos

def mostrar_menu_clientes(menu):
    print("\n--- MENÚ DISPONIBLE ---")
    if len(menu) == 0:
        print("No hay platos disponibles.")
    else:
        for i in range(len(menu)):
            plato = menu[i]
            print(f"{i + 1}. {plato[0]} - ${plato[1]} - {plato[2]}")

def registrar_pedido():
    menu = leer_menu()

    if len(menu) == 0:
        print("No hay platos en el menú para ordenar.")
        return

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    agregar_cliente(nombre_cliente)

    mostrar_menu_clientes(menu)
    opcion = int(input("Seleccione el número del plato que desea ordenar: ")) - 1

    if 0 <= opcion < len(menu):
        plato = menu[opcion]
        agregar_pedido(nombre_cliente, plato[0], plato[1])
        print("Pedido registrado correctamente.")
    else:
        print("Selección inválida.")

def mostrar_resultados():
    pedidos = leer_pedidos()
    print("\n--- RESULTADOS DE LOS PEDIDOS ---")

    if len(pedidos) == 0:
        print("No se han registrado pedidos.")
    else:
        total = 0
        for pedido in pedidos:
            print(f"Cliente: {pedido[0]} | Plato: {pedido[1]} | Precio: ${pedido[2]}")
            total += pedido[2]

        print(f"Cantidad de clientes: {len(pedidos)}")
        print(f"Total a pagar: ${total}")

def ver_menu():
    menu = leer_menu()
    mostrar_menu_clientes(menu)

def mostrar_menu_modulo_clientes():
    print("\n" + "-" * 35)
    print("MÓDULO CLIENTES")
    print("-" * 35)
    print("1. Ver menú")
    print("2. Realizar pedido")
    print("3. Ver resultados")
    print("4. Volver al menú principal")

def menu_clientes():
    while True:
        mostrar_menu_modulo_clientes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_menu()
        elif opcion == "2":
            registrar_pedido()
        elif opcion == "3":
            mostrar_resultados()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
