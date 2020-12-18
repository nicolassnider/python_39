import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()

estudiantes = [
    ('asdf0@mail.com','aaa','asda',26),
    ('asdf1@mail.com','aab','asdb',26),
    ('asdf2@mail.com','aac','asdc',27),
    ('asdf3@mail.com','aad','asdd',27),
    ('asdf4@mail.com','aae','asde',28)
]
cursor.executemany('INSERT INTO estudiante VALUES (?,?,?,?)',estudiantes)

conexion.commit()

conexion.close()