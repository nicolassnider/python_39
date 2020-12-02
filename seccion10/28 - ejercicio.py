def funcname(usuario, hsTrabajadas, valorHr):
    """
    docstring
    """
    print("%s va a cobrar %.3f por %d horas trabajadas" % (usuario, hsTrabajadas*valorHr, hsTrabajadas))
    pass


usuario = input("nombre usuario: ")
hsTrabajadas = int(input("horas trabajadas: "))
valorHr = float(input("valor hora: "))

funcname(usuario, hsTrabajadas, valorHr)

