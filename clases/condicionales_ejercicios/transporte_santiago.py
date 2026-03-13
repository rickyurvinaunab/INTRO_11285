lluvia = input()
congestion = input()
calidad_aire = input()

if lluvia == "si":
    print("El estudiante decide ir en Metro")
elif congestion == "si":
    print("El estudiante decide ir en bicicleta")
elif calidad_aire == "regular" or calidad_aire == "mala":
    print("El estudiante decide ir en Metro")
else:
    print("El estudiante decide ir en micro")