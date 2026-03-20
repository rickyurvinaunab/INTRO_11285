num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
operacion = input("Ingresa la operacion (+, -, *, /): ")

if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("No se puede dividir por cero")
else:
    print("Operacion invalida")