# Define una función calcular_imc que tome como parámetros el peso y la altura de una persona y
#  devuelva su índice de masa corporal (IMC). Luego, crea otra función llamada clasificar_imc 
# que clasifique el resultado del IMC usando las siguientes condicionales:
# IMC < 18.5: Bajo peso
# 18.5 ≤ IMC < 24.9: Peso normal
# 25 ≤ IMC < 29.9: Sobrepeso
# IMC ≥ 30: Obesidad

def calcular_imc(peso, altura):
    imc =  peso / altura**2

    return imc

def clasificar_imc(imc):
    if imc <18.5:
        return "Bajo peso"
    elif imc >= 18.5 and imc <24.9:
        return "Peso normal"
    elif imc>=25 and imc <29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"
    
#Programa principal

peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))

imc = calcular_imc(peso, altura)
resultado = clasificar_imc(imc)
print(resultado)