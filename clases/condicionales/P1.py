lluvia = input()
congesiton = input()
aire = input()

if lluvia == "si":
    print("El estudiante decide ir en Metro")
elif lluvia == "no" and congesiton == "si":
    print("El estudiante decide ir en bicicleta")
elif lluvia == "no" and congesiton == "no" and (aire == "regular" or aire == "mala"):
    print("El estudiante decide ir en Metro")
else:
    print("El estudiante decide ir en micro")