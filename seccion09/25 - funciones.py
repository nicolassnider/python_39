def funcname(par1, par2):
    """
    docstring
    """
    print("hola")

    print(par1,par2)
    pass

def funcname2(var1,var2 = "mundo"):
    """
    docstring
    """
    print(var1,var2)
    pass

def funcname3(var1, var2, *otros):
    """
    docstring
    """
    print("par1: ",var1)
    print("par2",var2)
    for par in otros:
        print("parametro:", par)
        pass
    pass

def f(x,y):
    """
    docstring
    """
    x=x+3
    y.append(23)
    print(x,y)
    pass

def sumar(n1,n2):
    """
    docstring
    """
    return n1+n2
    pass

funcname("hola","mundo")
funcname(par2="mundo", par1="hola")
funcname2(var1 = "hola")

funcname3("ana","curso", 1,2,3,4)

x=22
y=[22]
f(x,y)
print(x,y)

i = sumar(1,2)
print (i)