import os

ARCHIVO_MENU = "menu.txt"
ARCHIVO_CLIENTES = "clientes.txt"
ARCHIVO_PEDIDOS = "pedidos.txt"

def inicializar_archivos():
    if not os.path.exists(ARCHIVO_MENU):
        with open(ARCHIVO_MENU, "w", encoding="utf-8") as archivo:
            archivo.write("Ceviche;12.5;Entrada\n")
            archivo.write("Lomo Saltado;15.0;Fondo\n")
            archivo.write("Jugo Natural;4.5;Bebida\n")

    if not os.path.exists(ARCHIVO_CLIENTES):
        with open(ARCHIVO_CLIENTES, "w", encoding="utf-8") as archivo:
            pass

    if not os.path.exists(ARCHIVO_PEDIDOS):
        with open(ARCHIVO_PEDIDOS, "w", encoding="utf-8") as archivo:
            pass

def leer_menu():
    menu = []
    with open(ARCHIVO_MENU, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea != "":
                partes = linea.split(";")
                menu.append([partes[0], float(partes[1]), partes[2]])
    return menu

def guardar_menu(menu):
    with open(ARCHIVO_MENU, "w", encoding="utf-8") as archivo:
        for plato in menu:
            archivo.write(f"{plato[0]};{plato[1]};{plato[2]}\n")

def agregar_cliente(nombre_cliente):
    with open(ARCHIVO_CLIENTES, "a", encoding="utf-8") as archivo:
        archivo.write(nombre_cliente + "\n")

def leer_clientes():
    clientes = []
    with open(ARCHIVO_CLIENTES, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre = linea.strip()
            if nombre != "":
                clientes.append(nombre)
    return clientes

def agregar_pedido(nombre_cliente, nombre_plato, precio):
    with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre_cliente};{nombre_plato};{precio}\n")

def leer_pedidos():
    pedidos = []
    with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea != "":
                partes = linea.split(";")
                pedidos.append([partes[0], partes[1], float(partes[2])])
    return pedidos
