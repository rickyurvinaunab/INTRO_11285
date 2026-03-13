# import cimc
# from cimc import calcular_imc
from cimc import calcular_imc as ci
from cimc import calcular_area as ca

altura = float(input("Ingresa tu altura: "))
peso = float(input("Ingresa tu peso: "))

# imc = cimc.calcular_imc(altura, peso)
imc = ci(altura, peso)

print("Tu IMC es: ", imc)