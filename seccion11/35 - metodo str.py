class Auto:
    """Abstraccion de los objetos Autos"""
    def __init__(self, color, cantPuertas, nafta ):
        self.color= color
        self.cantPuertas = cantPuertas
        self.nafta= nafta

    def __str__(self):
        """Muestra el objeto en cuestion"""
        return "Este auto es " + self.color + " y tiene " + str(self.cantPuertas) + " puertas"

mi_auto = Auto("violeta", 5, 5)
print(mi_auto)
