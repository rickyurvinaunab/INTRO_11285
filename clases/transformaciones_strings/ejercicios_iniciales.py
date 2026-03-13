# 1. calcula el resultado de la expresion: (15 // 4) * 3 + 15 % 4. explica el orden en que se realizan las operaciones
resultado1 = (15 // 4) * 3 + 15 % 4
print("resultado1 es: ", resultado1)

#2. escribe una expresion que permita obtener el ultimo digito de un numero, por ejemplo de 9876
numero = 9876
ultimo_digito = numero % 10
print("ultimo_digito es:", ultimo_digito)

#3. si una persona tiene 25 anos, calcula cuantos meses ha vivido y cuantas semanas aproximadamente
edad_anos = 25
meses = edad_anos * 12
semanas_aprox = meses * 4
print("meses =", meses)
print("semanas aproximadas =", semanas_aprox)


# 1. si x = 5, transforma su valor sumandole 3 y multiplicando el resultado por 2. muestra el valor final
x = 5
y = (x + 3)
x = y * 2
print("resultado1 es:", x)

# 2. cual es el resultado de (7 < 10 o 7 >= 10)?
resultado2 = (7 < 10) or (7 >= 10)
print("resultado2 es:", resultado2)

# 3. la caja de 10 chocolates cuesta un valor que sera recibido como un input. cual es el costo final si le aplico un 40% de descuento? imprime el valor por pantalla
costo_chocolates = input("Ingrese el costo de la caja de 10 chocolates: ")
costo_chocolates = float(costo_chocolates)  # Convertir el input
costo_final = costo_chocolates * 0.6
print("costo_final es:", costo_final)
