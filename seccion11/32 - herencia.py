class Vehiculo:
    def __init__(self, tipo, color, cantPuertas, combustible):
        self.tipo= tipo
        self.color = color
        self.puertas = cantPuertas
        self.combustible = combustible

    def arrancar(self):
        if self.combustible > 0:
            print("arranca!")
        else:
            print("No arranca")

class Auto(Vehiculo):
    pass

miAuto = Auto("terretre","violeta",5,4)
miAuto.arrancar()
