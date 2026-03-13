from pizza import ingrediente_principal, ingrediente_secundario, precio_ingrediente

dia = input()

for i in range(10):
    nombre = input()
    i_p = ingrediente_principal(nombre)
    precio_i_p = precio_ingrediente(i_p, dia)
    i_s = ingrediente_secundario(nombre)
    precio_i_s = precio_ingrediente(i_s, dia)
    total = precio_i_p + precio_i_s

    if total <= 9990:
        print(nombre, total)