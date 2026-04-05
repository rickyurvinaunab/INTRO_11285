n = int(input())
i = 1
acumulado = 0

while i <= n:
    if i % 2 == 0:
        acumulado += i
    else:
        acumulado -= 1
    i += 1

print(acumulado)
