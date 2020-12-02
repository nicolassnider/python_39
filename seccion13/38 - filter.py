def es_par(n):
    return (n % 2 == 0)


l = [1, 2, 3, 4, 5, 6, 7, 8]

l2 = list(filter(es_par, l))
print(l2)
