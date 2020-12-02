personas = dict(nombre="ana", edad=55, pais="Argentina")

print(personas)

dict2 = dict(zip('abc',[1,2,3]))
print(dict2)

tupla = dict2.items()
print(tupla)

print(dict2.keys())
print(dict2.values())

dict2.clear()
print(dict2)

dict2 = dict(zip('abc',[1,2,3]))

valor = dict2.get('b')
print(valor)

dict2.pop('c')
print(dict2)

dict2 = dict(zip('abc',[1,2,3]))

aux = dict2.setdefault('a')
print(aux)

dict2.setdefault('e',100)
print(dict2)