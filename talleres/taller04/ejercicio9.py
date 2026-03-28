usuario = input("Ingrese usuario: ")

if usuario != "admin":
    print("Usuario incorrecto")
else:
    contrasena = input("Ingrese contrasena: ")

    if contrasena == "python123":
        print("Acceso concedido")
    else:
        print("Contrasena incorrecta")
