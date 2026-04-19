import os

ARCHIVO_MENU = "menu.txt"
ARCHIVO_CLIENTES = "clientes.txt"
ARCHIVO_PEDIDOS = "pedidos.txt"


def inicializar_archivos():

    if not os.path.exists(ARCHIVO_MENU):
        archivo = open(ARCHIVO_MENU, "w", encoding="utf-8")
        archivo.write("Ceviche;12.5;Entrada\n")
        archivo.write("Lomo Saltado;15.0;Fondo\n")
        archivo.write("Jugo Natural;4.5;Bebida\n")
        archivo.close()

    if not os.path.exists(ARCHIVO_CLIENTES):
        archivo = open(ARCHIVO_CLIENTES, "w", encoding="utf-8")
        archivo.close()

    if not os.path.exists(ARCHIVO_PEDIDOS):
        archivo = open(ARCHIVO_PEDIDOS, "w", encoding="utf-8")
        archivo.close()


def leer_menu():

    menu = []

    archivo = open(ARCHIVO_MENU, "r", encoding="utf-8")

    for linea in archivo:
        linea = linea.strip()

        if linea != "":
            partes = linea.split(";")
            menu.append([partes[0], float(partes[1]), partes[2]])

    archivo.close()

    return menu


def guardar_menu(menu):

    archivo = open(ARCHIVO_MENU, "w", encoding="utf-8")

    for plato in menu:
        archivo.write(plato[0] + ";" + str(plato[1]) + ";" + plato[2] + "\n")

    archivo.close()


def agregar_cliente(nombre_cliente):

    archivo = open(ARCHIVO_CLIENTES, "a", encoding="utf-8")
    archivo.write(nombre_cliente + "\n")
    archivo.close()


def leer_clientes():

    clientes = []

    archivo = open(ARCHIVO_CLIENTES, "r", encoding="utf-8")

    for linea in archivo:
        nombre = linea.strip()

        if nombre != "":
            clientes.append(nombre)

    archivo.close()

    return clientes


def agregar_pedido(nombre_cliente, nombre_plato, precio):

    archivo = open(ARCHIVO_PEDIDOS, "a", encoding="utf-8")
    archivo.write(nombre_cliente + ";" + nombre_plato + ";" + str(precio) + "\n")
    archivo.close()


def leer_pedidos():

    pedidos = []

    archivo = open(ARCHIVO_PEDIDOS, "r", encoding="utf-8")

    for linea in archivo:
        linea = linea.strip()

        if linea != "":
            partes = linea.split(";")
            pedidos.append([partes[0], partes[1], float(partes[2])])

    archivo.close()

    return pedidos