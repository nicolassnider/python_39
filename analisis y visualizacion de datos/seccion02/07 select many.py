import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.execute("SELECT * FROM estudiante")
estudiantes = cursor.fetchall()

for estudiante in estudiantes:
    print (estudiante)
    pass
