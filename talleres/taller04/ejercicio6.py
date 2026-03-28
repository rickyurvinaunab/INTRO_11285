usuario = input("Ingrese usuario: ")
contrasena = input("Ingrese contrasena: ")

if usuario == "bloqueado":
    print("Acceso denegado")
elif (usuario == "admin" or usuario == "supervisor") and contrasena == "1234":
    print("Acceso permitido")
else:
    print("Acceso denegado")
