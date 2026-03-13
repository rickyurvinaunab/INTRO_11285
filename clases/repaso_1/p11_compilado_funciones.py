# Escribe tu código aquí

from iva import tipo_item, tiene_iva, aplicar_iva, aplicar_descuento

dia_mes = int(input())
n = int(input())
total = 0
for i in range(n):
    nombre = input()
    precio = int(input())
    tipo = tipo_item(nombre)
    precio_mas_iva = precio
    if tipo == "comida":
        aplica_iva = tiene_iva(nombre)
        if aplica_iva:
            precio_mas_iva = aplicar_iva(precio)
    precio_con_descuento = aplicar_descuento(precio_mas_iva, dia_mes)
    total += precio_con_descuento

print(f"El total consumido hoy es {total}")