usuario = input("nombre usuario: ")
hsTrabajadas = int(input("horas trabajadas: "))
valorHr = float(input("valor hora: "))

print("%s va a cobrar %.3f por %d horas trabajadas" % (usuario, hsTrabajadas*valorHr, hsTrabajadas))