import numpy as np

arreglo = np.array([0,1,2,3,4,5])

arreglo, type(arreglo)


notas = [16,17,14,17,19,15]

print(type(notas))
ar_notas = np.array(notas, dtype=float)
print(type(ar_notas))
print(type(ar_notas[0]))

ar_notas_todas = np.array(([0,1,2,3,4,5], notas))
print(ar_notas_todas)

for nodo_nota in ar_notas_todas:
    print(nodo_nota)
    pass

print (ar_notas_todas.ndim)
print (ar_notas.ndim)

print (ar_notas_todas.shape) #cantidad de filas, cantidad de elementos en las filas