def ver_menu():
    print("\nMenu de platos\n")
    archivo = open("platos.txt","r")
    contenido = archivo.readlines()
    ['1500-2000-5000\n','0-0-0\n']
    archivo.close()
    lista_platos = []
    indice = 1
    for linea in contenido:
        datos = linea.strip().split("-")
        lista_platos.append(datos)
        print(f"{indice}.- {datos[0]} precio: {datos[1]} cat: {datos[1]}")
        indice += 1
    return [contenido, lista_platos]

    
def modulo_principal_adm():

    print("Modulo de admin")

    op_adm = -1
    while op_adm == -1:
        print()
        print()
        print("1. Crear platos")
        print("2. Modificar platos")
        print("3. Eliminar platos")
        print("4. Ver el menu")
        print("5. Salir al menu principal")

        op_adm = int(input("Ingresa la op_adm (1-3): "))
        
        if op_adm == 5:
            print("Saliendo al menu principal")
            return
        elif op_adm == 1:
            print()
            print("Creando un plato...")
            nombre = input("ingresa el nombre del plato: ")
            precio = input("ingresa el precio del plato: ")
            categoria = input("ingresa la categoria del plato: ")
            archivo = open("platos.txt","a") # w -> write o a -> append
            texto = nombre+"-"+precio+"-"+categoria+"\n"
            archivo.write(texto)
            archivo.close()
            print("Plato ingresado....")
        elif op_adm == 2:
            print()
            print("Modificando un plato...")
            resultado = ver_menu()
            contenido = resultado[0]
            lista_platos = resultado[1]
            num_plato = int(input("Ingrese el # de plato a modificar: "))
            while num_plato < 1 or num_plato > len(contenido):
                print("Opcion no valida, vuelva a ingresar: ")
                num_plato = int(input("Ingrese el # de plato a modificar: "))
            print("Plato a modificar es: ", contenido[num_plato-1])
            lista_platos[num_plato-1][0] = input("Ingresa el nombre del plato: ")
            lista_platos[num_plato-1][1] = input("Ingresa el precio del plato: ")
            lista_platos[num_plato-1][2] = input("Ingresa la categoria del plato: ")
            archivo = open("platos.txt","w")
            for plato in lista_platos:
                texto = plato[0]+"-"+plato[1]+"-"+plato[2]+"\n"
                archivo.write(texto)
            archivo.close()
            print("plato modificado exitosamente.")
        elif op_adm == 3:
            print()
            print("Eliminando un plato...")
            resultado = ver_menu()
            contenido = resultado[0]
            lista_platos = resultado[1]
            num_plato = int(input("Ingrese el # de plato a eliminar: "))
            while num_plato < 1 or num_plato > len(contenido):
                print("Opcion no valida, vuelva a ingresar: ")
                num_plato = int(input("Ingrese el # de plato a eliminar: "))
            print("Plato a eliminar es: ", contenido[num_plato-1])
            lista_platos.pop(num_plato-1)
            archivo = open("platos.txt","w")
            for plato in lista_platos:
                texto = plato[0]+"-"+plato[1]+"-"+plato[2]+"\n"
                archivo.write(texto)
            archivo.close()
        elif op_adm == 4:
            resultado = ver_menu()
            lista_platos = resultado[1]
            total = 0
            for plato in lista_platos:
                precio = int(plato[1])
                total += precio
            print("El precio total del menu es:", total)
        else:
            print("op_adm invalida")
        op_adm = -1

