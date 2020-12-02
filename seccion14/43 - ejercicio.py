class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return self.nombre + " tiene " + str(self.edad) + "años "

personas = [
        Persona("Pedro", 33),
        Persona("Ana", 9),
        Persona("Martin", 55),
        Persona("Juan", 10)
]

menoresEdad= filter( lambda p : p.edad < 18  , personas )

for menor in menoresEdad:
    print(menor)
    
