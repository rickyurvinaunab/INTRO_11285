from pizza import ingrediente_principal, ingrediente_secundario, precio_ingrediente, nombre_dia


def mejor_dia(ingrediente1, ingrediente2):
    valor_min = 10000000000
    dia_max = ""
    for i in range(1, 8):
        dia = nombre_dia(i)
        precio_i_p = precio_ingrediente(ingrediente1, dia)
        precio_i_s = precio_ingrediente(ingrediente2, dia)
        total = precio_i_p + precio_i_s
        if total < valor_min:
            valor_min = total
            dia_max = dia

    return dia_max