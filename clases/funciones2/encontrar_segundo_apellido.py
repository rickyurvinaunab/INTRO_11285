def encontrar_segundo_apellido(nombre):
    apellido = ""
    contador = 0
    for caracter in nombre:
        if caracter == " ":
            contador += 1
        if contador == 1 and caracter != " ":
            apellido += caracter
    return apellido

nombre = "ABEL BAEZ EMILIA MAGDALENA"
apellido = encontrar_segundo_apellido(nombre)
print("El segundo apellido obtenido de la función es:", apellido)