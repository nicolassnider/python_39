x = int(input("ingrese el valor de X: "))
y = int(input("ingrese el valor de y: "))
z = int(input("ingrese el valor de z: "))
n = int(input("ingrese el valor de N: "))


# devolver -->[i, j, k]

# i : 0<= i <= x  -->  range(0,x+1)
# j:  0<= j <= y --> range(0, y+1)
# k:  0<= k <= z  --> range(0, z+1)

# (i + j + k) != n

print(
    [
        [i, j, k] for i in range(0, x+1)
        for j in range(0, y+1)
        for k in range(0, z+1) if ((i + j + k) != n)
    ])
