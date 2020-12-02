def division(x,y):
    """
    docstring
    """
    try:
        return a/b
        pass
    except ZeroDivisionError:
        print("intenta dividir por 0")
        pass
    except NameError:
        print("la variable no es numérica")
    
    pass

division(1,"a")