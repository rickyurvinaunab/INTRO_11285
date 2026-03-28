tipo_cliente = input("Ingrese tipo de cliente (vip o regular): ")
monto_compra = float(input("Ingrese monto: "))

if monto_compra < 5000:
    print("No accede a la promocion")
elif tipo_cliente == "vip" or monto_compra >= 20000:
    print("Accede a la promocion")
else:
    print("No accede a la promocion")
