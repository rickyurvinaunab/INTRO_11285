#Entradas o Datos
distancia = int(input("Ingrese la distancia a recorrer: "))
consumo_litros_vehiculo = float(input("Ingresa el consumo de litros de tu vehículo: "))
precio_combustible = 1500
costo_peajes = 10000

#Solución
consumo_total = distancia * consumo_litros_vehiculo
costo_combustible = consumo_total * precio_combustible
costo_total = costo_combustible + costo_peajes

#Salida
print("El costo total del viaje es: ", costo_total, "CLP")