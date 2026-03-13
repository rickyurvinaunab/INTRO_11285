def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)

def suma_lista(lst):
    if len(lst) == 0:
        return 0
    else:
        primero = lst[0]
        resto = lst[1:]
        return primero + suma_lista(resto)

print("factorial(5):", factorial(5))     # 120
print("potencia(2, 10):", potencia(2, 10))
print("suma_lista([1,2,3,4]):", suma_lista([1, 2, 3, 4]))