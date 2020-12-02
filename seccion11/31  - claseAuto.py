class Auto:
    """
    docstring
    """

    def __init__(self, nafta):
        """
        docstring
        """
        self.nafta = nafta
        print("tenemos", nafta, "Lt")
        pass

    def Arrancar(self):
        """
        docstring
        """
        if self.nafta>0:
            print("arranca")
            pass
        else:
            print("no arranca, sin nafta")
    pass

    def Andar(self):
        """
        docstring
        """
        if self.nafta>0:
            self.nafta= self.nafta - 1
            print("andando... quedan",self.nafta,"lt")
            print(self.nafta)
            pass
        else:
            print("no anda, sin nafta")
            pass
        pass

    pass


miAuto = Auto(40)
miAuto.Arrancar()
for i in range(1,50):
    miAuto.Andar()
    pass
