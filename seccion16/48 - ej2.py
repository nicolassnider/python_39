def filtrarPalabras(lista1, entero):
    """
    docstring
    """
    for el in lista1:
        if len(el)>= entero:
            print(el)
            pass
        pass
    pass

filtrarPalabras(["a","abc","abcd","abcdef","abcdefg"], 4)