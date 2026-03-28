nota = float(input("Ingrese la nota: "))

if nota < 1.0 or nota > 7.0:
    print("Nota invalida")
elif nota < 4.0:
    print("Insuficiente")
elif nota <= 4.9:
    print("Suficiente")
elif nota <= 5.9:
    print("Bueno")
else:
    print("Excelente")
