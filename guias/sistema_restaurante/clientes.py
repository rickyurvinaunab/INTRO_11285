def mostrar_menu_clientes(menu_restaurante):
    print("\n--- MENU DISPONIBLE ---")
    if len(menu_restaurante) == 0:
        print("No hay platos disponibles.")
    else:
        for i in range(len(menu_restaurante)):
            plato = menu_restaurante[i]
            print(f"{i + 1}. {plato[0]} - ${plato[1]} - {plato[2]}")

def registrar_pedido(menu_restaurante, pedidos):
    if len(menu_restaurante) == 0:
        print("No hay platos en el menu para ordenar.")
        return

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    mostrar_menu_clientes(menu_restaurante)

    opcion = int(input("Seleccione el número del plato que desea ordenar: ")) - 1

    if 0 <= opcion < len(menu_restaurante):
        plato = menu_restaurante[opcion]
        pedidos.append([nombre_cliente, plato[0], plato[1]])
        print("Pedido registrado correctamente.")
    else:
        print("Selección inválida.")

def mostrar_resultados(pedidos):
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

def mostrar_menu_modulo_clientes():
    print("\n" + "-" * 35)
    print("MÓDULO CLIENTES")
    print("-" * 35)
    print("1. Ver menú")
    print("2. Realizar pedido")
    print("3. Ver resultados")
    print("4. Volver al menú principal")

def menu_clientes(menu_restaurante, pedidos):
    while True:
        mostrar_menu_modulo_clientes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_menu_clientes(menu_restaurante)
        elif opcion == "2":
            registrar_pedido(menu_restaurante, pedidos)
        elif opcion == "3":
            mostrar_resultados(pedidos)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
