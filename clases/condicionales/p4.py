anio = int(input("Ingresa un anio: "))

if anio % 400 == 0:
    print("Es bisiesto")
elif anio % 100 == 0:
    print("No es bisiesto")
elif anio % 4 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")