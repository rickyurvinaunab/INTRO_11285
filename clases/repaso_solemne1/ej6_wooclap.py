total = 0
contador = 0
for i in range(1, 4):
    for j in range(1, 3):
        if i == j:
            total += 2
        else:
            total += 1

print(total)
