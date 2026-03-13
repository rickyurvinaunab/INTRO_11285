# tarifa = 790
# saldo = 13850
# viajes = 0

# while saldo >= tarifa:
#     saldo -= tarifa
#     viajes += 1
#     print(f"Viaje #{viajes} | Saldo: {saldo}")

# print(f"Viajes realizados: {viajes} | Saldo restante: {saldo}")


tarifa = 790
saldo = 13850
viajes = 0
while saldo >= tarifa:
    saldo -= tarifa
    viajes += 1
    print(f"Viaje #{viajes} | Saldo: {saldo}")
    # Me aburro despues de 10 viajes
    if viajes == 10:
        print("Me aburri en Baquedano, ¡me bajo del metro!")
        break
print(f"Viajes realizados: {viajes} | Saldo final: {saldo}")