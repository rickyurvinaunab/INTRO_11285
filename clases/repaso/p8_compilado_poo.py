# Clase que representa una planta
class Planta:

    # Metodo constructor, inicializa el nombre, el agua y la resistencia de la planta
    def __init__(self, nombre, resistencia):
        self.nombre = nombre
        self.agua = 0
        self.resistencia = resistencia

    # Metodo para mostrar la planta como cadena de texto
    def __str__(self):
        return f"{self.nombre} - {self.agua}/{self.resistencia}"

    # Metodo para regar la planta con una cantidad de agua
    def regar(self, agua):
        suma = agua + self.agua
        # Si la suma de agua no supera la resistencia, se agrega el agua
        if suma <= self.resistencia:
            self.agua += agua
        # Si supera la resistencia, el agua se iguala a la resistencia maxima
        else:
            self.agua = self.resistencia