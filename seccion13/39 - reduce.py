from functools import reduce
def sumar(x,y):
    """
    docstring
    """
    return x+y
    pass

lista = range(1,1000)

l2=reduce(sumar, lista)
print(l2)