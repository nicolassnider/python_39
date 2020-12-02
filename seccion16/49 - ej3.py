#Pedirle al usuario que ingrese por pantalla una cadena, el programa evalua la cadena
#y devuelve cuantas letras mayusculas tiene

cadena = input("Ingrese una cadena: ")

def analizar(cadena):
    cont= 0
    for i in cadena:
        if i != i.lower():
            cont += 1
    print("La cadena tiene ", cont , " mayusculas")

print(analizar(cadena))
