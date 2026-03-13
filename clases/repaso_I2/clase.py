# 1. pensar estrategia
# 2. caso base


notas = [3,4,5]
def calcular_promedio(notas, contador, suma):

    if contador == len(notas):
        return suma/contador

    return calcular_promedio(notas, contador+1, suma+notas[contador])
# calcular_promedio([3,4,5], 0+1, 0+3)
# calcular_promedio([3,4,5], 1+1, 3+4)
# calcular_promedio([3,4,5], 2+1, 7+5)
# calcular_promedio([3,4,5], 3, 7+5)
# calcular_promedio(12/3)

print(calcular_promedio(notas,0, 0))
        
