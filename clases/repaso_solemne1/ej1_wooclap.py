numero = int(input())
total = 0

for i in range(1, 5):
    if numero > 0:
        total += i
    elif numero == 0:
        total += 2
    else:
        total -= i

print(total)
