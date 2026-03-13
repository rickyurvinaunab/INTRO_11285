# Escribe tu código aquí

a = float(input())
b = float(input())
c = float(input())

discriminante = b ** 2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print("Todos los numeros son solucion")
elif a == 0 and b == 0:
    print("Sin solucion")
elif a == 0:
    solucion_unica = -c / b
    print("Una solucion:", solucion_unica)
elif discriminante > 0:
    solucion1 = (-b + (discriminante) ** 0.5) / (2 * a)
    solucion2 = (-b - (discriminante) ** 0.5) / (2 * a)
    print("La ecuacion tiene dos soluciones:", solucion1, " y ", solucion2)
elif discriminante == 0:
    solucion_unica = -b / (2 * a)
    print("Una solucion:", solucion_unica)
else:
    print("Sin solucion real")

