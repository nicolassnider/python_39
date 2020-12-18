import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.execute('CREATE TABLE estudiante(email VARCHAR(100),carrera VARCHAR(100),nombre VARCHAR(100), edad INTEGER)')

conexion.close()