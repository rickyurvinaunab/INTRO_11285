numero = int(input("Ingrese un numero de tres digitos: "))
primer_digito = numero // 100
ultimo_digito = numero % 10
suma = primer_digito + ultimo_digito
print("Primer digito:", primer_digito)
print("Ultimo digito:", ultimo_digito)
print("Suma:", suma)
