oracion = "el payaso corrio tras el coche y el coche corrio hacia la carpa y la carpa cayo sobre el payaso y el coche"

palabras = oracion.lower().split()

palabras_unicas = []
repeticiones = []

for palabra in palabras:
    if palabra in palabras_unicas:
        idx = palabras_unicas.index(palabra)
        repeticiones[idx] += 1
    else:
        palabras_unicas.append(palabra)
        repeticiones.append(1)

max_repeticiones = max(repeticiones)
idx_max = repeticiones.index(max_repeticiones)
palabra_mas_repetida = palabras_unicas[idx_max]

print(f"Numero total de palabras: {len(palabras)}")
print(f"La palabra que mas se repite es '{palabra_mas_repetida}")