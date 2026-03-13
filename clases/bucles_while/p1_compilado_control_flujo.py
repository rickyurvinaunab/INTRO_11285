cant = 220
edad = int(input())
fcm = cant - edad
reposo   = 0
moderada = 0
maxima   = 0
freq = int(input())
while freq != -1: # mientras la frecuencia no sea -1
    p_fcm = freq/fcm*100
    if p_fcm <= 55:
        reposo += 1
    elif p_fcm >= 95:
        maxima += 1
    else:
        moderada += 1
    freq = int(input())
print(f"Reposo: {reposo}")
print(f"Moderada: {moderada}")
print(f"Maxima: {maxima}")