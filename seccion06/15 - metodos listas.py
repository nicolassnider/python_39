lista = [0,1,2,3,4,5,6,7,8]
print (lista)

lista.append(9)
print (lista)


print("count ", lista.count(1))


lista2 = [10,11,12]
lista.extend(lista2)
print("extend: ",lista)

print("index", lista.index(5))

lista.insert(6,100)
print("insert ", lista)

lista.pop(6)
print("pop", lista)

lista.remove(8)
print("remove", lista)

lista.reverse()
print("reverse", lista)

lista.sort()
print("sort", lista)

lista.sort(reverse=True)
print("sort(reverse=True)", lista)