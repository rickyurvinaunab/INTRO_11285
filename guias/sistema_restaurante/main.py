from administrador import menu_administrador
from clientes import menu_clientes

def mostrar_menu_principal():
    print("\n" + "=" * 40)
    print("SISTEMA DEL RESTAURANTE")
    print("=" * 40)
    print("1. Modulo administrador")
    print("2. Modulo clientes")
    print("3. Salir")

def main():
    menu_restaurante = [
        ["Ceviche", 12.5, "Entrada"],
        ["Lomo Saltado", 15.0, "Fondo"],
        ["Jugo Natural", 4.5, "Bebida"]
    ]
    pedidos = []

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opcion (1-3): ")

        if opcion == "1":
            menu_administrador(menu_restaurante)
        elif opcion == "2":
            menu_clientes(menu_restaurante, pedidos)
        elif opcion == "3":
            print("Gracias por usar el sistema.")
            break
        else:
            print("ingrese nuevamente la opcion")


main()
