import sqlite3
import csv

conexion = sqlite3.connect('ejemplo.db')
cursor = conexion.cursor()

archivo = open(r"E:\Repos\python_39\analisis y visualizacion de datos\seccion02\archivo.txt")

filas = csv.reader(archivo)

cursor.executemany('INSERT INTO estudiante VALUES (?,?,?,?)',filas)

conexion.commit()

estudiantes = cursor.execute("SELECT * FROM estudiante")
print(estudiantes.fetchall())

conexion.commit()
conexion.close()