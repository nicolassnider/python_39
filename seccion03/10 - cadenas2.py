cadena = "hola mundo"
resultado = cadena.capitalize()
print(resultado)

resultado = cadena.count('o')
print(resultado)

resultado = cadena.endswith('do')
print(resultado)

resultado = cadena.endswith('da')
print(resultado)

resultado = cadena.find('do')
print(resultado)

resultado = cadena.isnumeric()
print(resultado)

cadena2=cadena
resultado = cadena2.replace('do','da')
print(resultado)

cadena3 = "    "+cadena+"    "
resultado = cadena3.strip()
print(resultado)

resultado = cadena.upper()
print(resultado)

resultado = cadena.lower()
print(resultado)

resultado = cadena.zfill(20)
print(resultado)
