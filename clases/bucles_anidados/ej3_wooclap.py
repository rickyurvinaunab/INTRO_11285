x = int(input())
resultado = 0

for i in range(3):
    if x > 5:
        if i % 2 == 0:
            resultado += x
        else:
            resultado -= 2
    else:
        resultado += 1

print(resultado)
