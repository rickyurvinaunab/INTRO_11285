# Ejercicio: sumar positivos y negativos de una lista

# ----------- CASO 1 -----------
lista = [10, -5, 7, -3]
dep_total = 0
ret_total = 0
for i in range(len(lista)):
    numero = lista[i]
    if numero > 0:
        dep_total = dep_total + numero
    else:
        ret_total = ret_total + numero
lista_respuesta = [dep_total, ret_total]
print("Lista:", lista)
print("Resultado:", lista_respuesta)


# casos de uso
# lista = [4, 8, -2, -6, 3]

# lista = [-1, -2, -3]

