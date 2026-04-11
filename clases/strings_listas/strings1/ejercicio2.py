# Escribe tu código aquí
p = input()
q = input()

mayusculas = "AEIOU"
son_llave = True

for i in range(len(p)):
    if (p[i] in mayusculas) != (q[i] in mayusculas):
        son_llave = False
        break

if son_llave:
    print("Si son llave")
else:
    print("No son llave")

# p = "aEi"
# q = "uOo"
# → True
#
# p = "aEi"
# q = "Uoo"
# → False
#
# p = "AEI"
# q = "UOO"
# → True
#
# p = "AiUe"
# q = "OoAa"
# → True
#
# p = "AiUe"
# q = "ooaa"
# → False