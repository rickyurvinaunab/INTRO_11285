# Clase que representa un huerto
class Huerto:

    # Metodo constructor, inicializa la lista de plantas
    def __init__(self):
        self.plantas = []

    # Metodo para regar una planta especifica por su nombre
    def regar_planta(self, nombre, agua):
        for planta in self.plantas:
            # Si el nombre coincide, riega la planta con la cantidad de agua indicada
            if nombre == planta.nombre:
                planta.regar(agua)
                break

    # Metodo para plantar una nueva planta en el huerto
    def plantar(self, planta):
        encontrado = False
        # Verifica si ya existe una planta con el mismo nombre
        for pl in self.plantas:
            if pl.nombre == planta.nombre:
                encontrado = True

        # Si no existe, agrega la planta y la riega con 5 unidades de agua
        if encontrado == False:
            self.plantas.append(planta)
            planta.regar(5)