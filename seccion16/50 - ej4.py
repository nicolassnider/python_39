#Pedir una lista con un conjunto de nombres, imprimir la cantidad de nombres
# que comienzan con la letra pasada por parametro


def calcular():
    num = int(input("Cuantos nombres vas a ingresar? "))
    lista = []
    for i in range(num):
        nombre = input("dame un nombre: ")
        lista.append(nombre)

    letra = input("Pasame la letra para controlar: ")
    cont = 0
    for nom in lista:
        if nom[0] == letra.lower() or nom[0]==letra.upper():
            cont += 1
    return cont

print(calcular())


