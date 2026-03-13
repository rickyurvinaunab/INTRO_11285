# El programa siguiente pide un número positivos al usuario y
# almacena la respuesta en la variable "numero". Después comprueba
# si el número es negativo. Si lo es, el programa avisa que no
# era eso lo que se había pedido. Finalmente, el programa imprime
# siempre el valor introducido por el usuario.

numero = int(input("Escriba un numero positivo: "))
if numero < 0:
    print("¡Le he dicho que escriba un numero positivo!")
print("Ha escrito el numero", numero)