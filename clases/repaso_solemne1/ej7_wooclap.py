i = 1
total = 0
contador = 0
while i <= 3:
    j = 1
    while j <= 2:
        if i + j > 3:
            total += 2
        else:
            total += 1
        j += 1
    i += 1

print(total)
