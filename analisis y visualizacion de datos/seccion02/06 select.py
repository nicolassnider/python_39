import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.execute("SELECT * FROM estudiante")
estudiante = cursor.fetchone()

print(estudiante)
print(len(estudiante))

for e in estudiante:
    print(e)
    pass