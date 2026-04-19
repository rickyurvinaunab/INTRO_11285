from utilidades import leer_menu, guardar_menu

def mostrar_menu(menu):
    print("\n--- MENÚ DEL RESTAURANTE ---")
    if len(menu) == 0:
        print("No hay platos registrados.")
    else:
        for i in range(len(menu)):
            plato = menu[i]
            print(f"{i + 1}. Nombre: {plato[0]} | Precio: ${plato[1]} | Categoría: {plato[2]}")

def crear_plato():
    menu = leer_menu()
    print("\n--- CREAR PLATO ---")
    nombre = input("Ingrese el nombre del plato: ")
    precio = float(input("Ingrese el precio del plato: "))
    categoria = input("Ingrese la categoría del plato: ")
    menu.append([nombre, precio, categoria])
    guardar_menu(menu)
    print("Plato agregado correctamente.")

def modificar_plato():
    menu = leer_menu()
    print("\n--- MODIFICAR PLATO ---")
    mostrar_menu(menu)

    if len(menu) == 0:
        return

    indice = int(input("Ingrese el número del plato que desea modificar: ")) - 1

    if 0 <= indice < len(menu):
        nombre = input("Nuevo nombre del plato: ")
        precio = float(input("Nuevo precio del plato: "))
        categoria = input("Nueva categoría del plato: ")

        menu[indice][0] = nombre
        menu[indice][1] = precio
        menu[indice][2] = categoria

        guardar_menu(menu)
        print("Plato modificado correctamente.")
    else:
        print("Número de plato inválido.")

def eliminar_plato():
    menu = leer_menu()
    print("\n--- ELIMINAR PLATO ---")
    mostrar_menu(menu)

    if len(menu) == 0:
        return

    indice = int(input("Ingrese el número del plato que desea eliminar: ")) - 1

    if 0 <= indice < len(menu):
        eliminado = menu.pop(indice)
        guardar_menu(menu)
        print(f"Plato eliminado: {eliminado[0]}")
    else:
        print("Número de plato inválido.")

def ver_menu():
    menu = leer_menu()
    mostrar_menu(menu)

def mostrar_menu_administrador():
    print("\n" + "-" * 35)
    print("MÓDULO ADMINISTRADOR")
    print("-" * 35)
    print("1. Crear plato")
    print("2. Modificar plato")
    print("3. Eliminar plato")
    print("4. Ver menú")
    print("5. Volver al menú principal")

def menu_administrador():
    while True:
        mostrar_menu_administrador()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_plato()
        elif opcion == "2":
            modificar_plato()
        elif opcion == "3":
            eliminar_plato()
        elif opcion == "4":
            ver_menu()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
