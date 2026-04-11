texto = ""

cadena = input("Inresa la cadena: ")
carcter_ant = cadena[0]
for caracter in cadena:

    if caracter != carcter_ant:
        texto += carcter_ant
    
    carcter_ant = caracter

print(texto+cadena[-1])

# casos de uso
# input
# EEEEEssstoooyy iiiintennntannndoooo     habbbbllaaarr
# output
# Estoy intentando hablar

# input
# hola     mundo
# output
# hola mundo