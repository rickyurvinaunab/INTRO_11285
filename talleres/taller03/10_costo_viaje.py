distancia_km = float(input("Ingrese la distancia del viaje en km: "))
consumo_km_litro = float(input("Ingrese el consumo del auto (km por litro): "))
precio_combustible = float(input("Ingrese el precio del combustible por litro: "))
costo_peajes = float(input("Ingrese el costo de peajes: "))
litros_necesarios = distancia_km / consumo_km_litro
costo_combustible = litros_necesarios * precio_combustible
costo_total_viaje = costo_combustible + costo_peajes
print("El costo total del viaje es:", costo_total_viaje)
