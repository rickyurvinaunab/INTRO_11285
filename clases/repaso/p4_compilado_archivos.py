# Funcion que escribe un archivo con los restaurantes que ofrecen un plato especifico y su precio
def escribir_deliveries(p):
    # Abre el archivo con los datos de los restaurantes en modo lectura
    archivo_r = open('restaurantes.txt','r')
    # Lee todas las lineas del archivo
    contenido_r = archivo_r.readlines()
    # Cierra el archivo despues de leer
    archivo_r.close()
    # Lista para guardar los resultados
    lista_resultado = []
    # Recorre cada restaurante en el contenido
    for restaurante in contenido_r:
        # Elimina espacios y divide la linea por ';'
        datos = restaurante.strip().split(';')
        # Obtiene el nombre del restaurante
        nombre_r = datos[0]
        # Obtiene la lista de platos
        platos = datos[1].split('-')
        # Obtiene la lista de precios
        precios = datos[2].split('-')
        # Verifica si el plato p esta en la lista de platos
        if p in platos:
            # Busca la posicion del plato en la lista
            posicion_p_en_platos = platos.index(p)
            # Obtiene el precio correspondiente
            precio = precios[posicion_p_en_platos]
            # Agrega el nombre y el precio a la lista de resultados
            lista_resultado.append([nombre_r, precio])
    # Formatea cada resultado como una cadena separada por ';' y agrega salto de linea
    for i in range(len(lista_resultado)):
        lista_resultado[i] = ';'.join(lista_resultado[i])+'\n'
        # print(lista_resultado[i])
    # Crea un archivo con el nombre del plato
    nombre_archivo = p+".txt"
    # Abre el nuevo archivo en modo escritura
    archivo_p = open(nombre_archivo, 'w')
    # Escribe los resultados en el archivo
    archivo_p.writelines(lista_resultado)
    # Cierra el archivo
    archivo_p.close()