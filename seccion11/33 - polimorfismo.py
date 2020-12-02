class Vehiculos:
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

class Auto(Vehiculos):
    pass

class Moto(Vehiculos):
    pass

class Barco(Vehiculos):
    pass

miAuto = Auto("terrestre","violeta","5",4)
miAuto.arrancar()

miMoto = Moto("terrestre","negro","0",2)
miMoto.arrancar()

miBarco = Barco("acuatico","blanco","0",0)
miBarco.arrancar()
