def mostrar_menu(menu_restaurante):
    print("\n--- MENÚ DEL RESTAURANTE ---")
    if len(menu_restaurante) == 0:
        print("No hay platos registrados.")
    else:
        for i in range(len(menu_restaurante)):
            plato = menu_restaurante[i]
            print(f"{i + 1}. Nombre: {plato[0]} | Precio: ${plato[1]} | Categoría: {plato[2]}")

def crear_plato(menu_restaurante):
    print("\n--- CREAR PLATO ---")
    nombre = input("Ingrese el nombre del plato: ")
    precio = float(input("Ingrese el precio del plato: "))
    categoria = input("Ingrese la categoría del plato: ")
    menu_restaurante.append([nombre, precio, categoria])
    print("Plato agregado correctamente.")

def modificar_plato(menu_restaurante):
    print("\n--- MODIFICAR PLATO ---")
    mostrar_menu(menu_restaurante)

    if len(menu_restaurante) == 0:
        return

    indice = int(input("Ingrese el número del plato que desea modificar: ")) - 1

    if 0 <= indice < len(menu_restaurante):
        nombre = input("Nuevo nombre del plato: ")
        precio = float(input("Nuevo precio del plato: "))
        categoria = input("Nueva categoría del plato: ")

        menu_restaurante[indice][0] = nombre
        menu_restaurante[indice][1] = precio
        menu_restaurante[indice][2] = categoria

        print("Plato modificado correctamente.")
    else:
        print("Número de plato inválido.")

def eliminar_plato(menu_restaurante):
    print("\n--- ELIMINAR PLATO ---")
    mostrar_menu(menu_restaurante)

    if len(menu_restaurante) == 0:
        return

    indice = int(input("Ingrese el número del plato que desea eliminar: ")) - 1

    if 0 <= indice < len(menu_restaurante):
        eliminado = menu_restaurante.pop(indice)
        print(f"Plato eliminado: {eliminado[0]}")
    else:
        print("Número de plato inválido.")

def mostrar_menu_administrador():
    print("\n" + "-" * 35)
    print("MÓDULO ADMINISTRADOR")
    print("-" * 35)
    print("1. Crear plato")
    print("2. Modificar plato")
    print("3. Eliminar plato")
    print("4. Ver menú")
    print("5. Volver al menú principal")

def menu_administrador(menu_restaurante):
    while True:
        mostrar_menu_administrador()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_plato(menu_restaurante)
        elif opcion == "2":
            modificar_plato(menu_restaurante)
        elif opcion == "3":
            eliminar_plato(menu_restaurante)
        elif opcion == "4":
            mostrar_menu(menu_restaurante)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
