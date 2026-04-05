edad = int(input())
suma = 0

for i in range(2, 7):
    if edad >= 18:
        if i % 3 == 0:
            suma += i
        else:
            suma += 1
    else:
        suma -= 2

print(suma)
