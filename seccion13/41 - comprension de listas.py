# Comprension de Listas
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [n ** 2 for n in l]
print(l)
print(l2)

l3 = [n for n in l if n % 2 == 0]
print(l3)
