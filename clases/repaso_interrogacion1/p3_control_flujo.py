# Escribe tu código aquí

x = int(input()) #recibo el valor de x, limite inferior
y = int(input()) #recibo el valor de y, limite superior
num = int(input()) # recibo el primer # de la secuencia
# indefinida de numeros
contador = 0 # inicializo un contador en cero, este ira
#aumentando cuando vaya recibiendo numeros que esten en el
#rango de x e y
while num != -1: # realizo un bucle indefinido
#mientras el num sea diferente de -1
    if num>=x and num <=y: #valido si el numero recibido esta entre x e y
        contador += 1 # si si esta, aumento en 1 el contador
    num = int(input()) #sigo recibiendo los numeros de la secuencia indefinida
print(contador) #despues que se acaba el bucle, imprimo el contador