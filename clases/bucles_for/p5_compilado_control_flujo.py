cantidad = int(input())

no_dino = 0
t_rex = 0
velo = 0
trice = 0

for i in range(cantidad):
    fosil = int(input())
    if fosil == 0:
        no_dino+=1
    elif fosil == 1:
        t_rex+=1
    elif fosil == 2:
        velo+=1
    elif fosil == 3:
        trice+=1

print("T-Rex:", t_rex)
print("Velociraptor:", velo)
print("Triceratops:", trice)