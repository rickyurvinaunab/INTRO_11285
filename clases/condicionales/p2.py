a = float(input())
b = float(input())
c = float(input())

if a == 0 and b == 0 and c == 0:
    print("Todos los numeros son solucion")

elif a == 0 and b == 0:
    print("No tiene solucion")
elif a == 0:
    x = -c / b
    print("Una solucion:", x)

else:
    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-b - d**0.5) / (2*a)
        x2 = (-b + d**0.5) / (2*a)

        if x1 < x2:
            print("Dos soluciones:", x1, "y", x2)
        else:
            print("Dos soluciones:", x2, "y", x1)

    elif d == 0:
        x = -b / (2*a)
        print("Una solucion:", x)

    else:
        print("No tiene solucion")