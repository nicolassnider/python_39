class Comprador:
        def __init__(self, nombre):
            self.nombre = nombre
            self.__nroCuenta = 12345

        def getnrocuenta(self):
            print(self.__nroCuenta)

        def setnroCuenta(self, valor):
            self.__nroCuenta = valor
            print(self.__nroCuenta)

        def __debitar(self):
            print("Debito es privado")


persona1 = Comprador("Pedro")
#print(persona1.__nroCuenta())
persona1.getnrocuenta()
persona1.setnroCuenta(9999)

#persona1.__debitar()
persona1._Comprador__debitar()
