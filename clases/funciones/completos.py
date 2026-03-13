# def hacer_completo():
#     print("Abrir pan")
#     print("Poner mayonesa")
#     print("Agregar palta, tomate y mayo")
#     print("Servir completo italiano")


# hacer_completo()
# print("Un segundo completo..")
# hacer_completo()








# def hacer_completo(tipo):
#     print("Abrir pan")
#     print("Poner mayonesa")
    
#     if tipo == "italiano":
#         print("Agregar palta, tomate y mayo")
#     elif tipo == "dinámico":
#         print("Agregar americana, mayo y kétchup")
#     else:
#         print("Agregar solo vienesa")
    
#     print(f"Servir completo {tipo}")

# hacer_completo("italiano")
# hacer_completo("dinámico")
# hacer_completo("americano")











def precio_completo(tipo):
    if tipo == "italiano":
        return 2000
    elif tipo == "dinámico":
        return 1800

total = precio_completo("dinámico")
print("Total a pagar:", total)
total2 = precio_completo("italiano")
print("Total a pagar2:", total2)
total3 = precio_completo("americano")
print("Total a pagar3:", total3)
