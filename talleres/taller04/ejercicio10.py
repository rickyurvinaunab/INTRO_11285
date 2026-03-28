import math

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

if a == 0 and b == 0 and c == 0:
    print("Todos los numeros son solucion")
elif a == 0 and b == 0 and c != 0:
    print("No tiene solucion")
elif a == 0:
    x = -c / b
    print("Es una ecuacion lineal")
    print("La solucion es:", x)
else:
    discriminante = b ** 2 - 4 * a * c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print("Tiene dos soluciones reales")
        print("x1 =", x1)
        print("x2 =", x2)
    elif discriminante == 0:
        x = -b / (2 * a)
        print("Tiene una solucion real")
        print("x =", x)
    else:
        print("No tiene soluciones reales")
