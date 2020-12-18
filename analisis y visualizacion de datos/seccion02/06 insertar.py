import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.execute("INSERT INTO estudiante VALUES('asd@mail.com','Artes','Sharon',27)")
conexion.commit()

conexion.close()