lista = [12, True,"hola", "ola q ase",[123.4,"hola Mundo!",7]]

for val in lista:
    print(val)
    pass

for val in lista[4]:
    print(val)
    pass

lista[1] = False

for val in lista:
    print(val)
    pass

print(lista[-1])
print(lista[-2])

print(lista[0:3])

print(lista[0:5:2])