#Escriba una funcion es_bisiesto() que determina si un año es es_bisiesto
# un año es bisiesto si es divisible por 4 pero no por 100
# o, si es divisible por 400


def es_bisiesto():
    a = int(input("ingrese un año para chequeo: "))

    if (a % 4 ==0 ) and (not(a % 100 == 0) ):
        print("El año ", a, " es bisiesto")
    elif (a % 400 == 0):
        print("El año ", a, " es bisiesto")
    else:
        print("El año ", a, " NO es bisiesto")


print(es_bisiesto())
