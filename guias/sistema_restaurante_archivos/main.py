from administrador import menu_administrador
from clientes import menu_clientes
from utilidades import inicializar_archivos

def mostrar_menu_principal():
    print("\n" + "=" * 40)
    print("SISTEMA DEL RESTAURANTE")
    print("=" * 40)
    print("1. Módulo administrador")
    print("2. Módulo clientes")
    print("3. Salir")

def main():
    inicializar_archivos()

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_administrador()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
