# import administrador

from administrador import modulo_principal_adm

opcion = -1
while opcion == -1:
    print("Bienvenido")
    print("1. Mod Administrador")
    print("2. Mod Clientes")
    print("3. Salir")

    opcion = int(input("Ingresa la opcion (1-3): "))
    
    if opcion == 3:
        print("Saliendo del sistema...")
        break
    elif opcion == 1:
        modulo_principal_adm()
    elif opcion == 2:
        print("Modulo de clientes")
    else:
        print("Opcion invalida")
    opcion = -1