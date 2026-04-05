n = int(input())
pasos = 0

while n > 0:
    if n % 2 == 0:
        n -= 2
    elif n == 1:
        n -= 1
    else:
        n -= 3
    pasos += 1

print(pasos)
