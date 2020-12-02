def Cuadrado(n):
    return n **2

lista = [1,2,3,4]
lista2 = list(map(Cuadrado,lista))

print(lista2)