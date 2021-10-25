import sqlite3 as dbapi  # importamos la librería de sqlLite

print(dbapi.version)
print(dbapi.threadsafety)  # Como es de seguro el uso de este hilo (de 0 a 3 en función de lo seguro que sea)
print(dbapi.paramstyle)  # para comprobar las consultas antes del procesado (SQLinjection)

"""
Standar Error
     |
     |Warning
     |
     |Error
       |
       |InterfaceError
       |
       |DatabaseError
            |
            |DataError
            |
            |OperationError
            |
            |IntegrityError
            |
            |InternalError
            |
            |ProgrunningError
            |
            |NotSupportedError
"""

try:
    bbdd = dbapi.connect(
        "BaseDatos.dat")  # Se le pasa como parámetro el fichero de la base de datos, si no existe lo crea
    # print(bbdd)
    cursor = bbdd.cursor()
    """cursor.execute("CREATE TABLE usuarios (dni text,"
                   "nombre text,"
                   "direccion text)")"""
    """cursor.execute("INSERT INTO usuarios VALUES ('36171305x','Angel','Florida')")
    cursor.execute("INSERT INTO usuarios VALUES ('36171306x','Pepe','Fragoso')")
    bbdd.commit()"""  # El commit hay que hacerlo para hacerlos efectivos
    # cursor.execute("SELECT * FROM usuarios")

    # SQL INJECTION
    dni = "36171305x"
    sqlInject = "'or '1' = '1"
    cursor.execute(f"SELECT * FROM usuarios WHERE  dni ='{dni}' + '{sqlInject}' ")


    def consultaSelect():
        for i in cursor.fetchall():
            print("Dni: " + i[0] + " Nombre: " + i[1] + " Dirección: " + i[2])

except dbapi.DatabaseError as e:
    print("Error en base de datos: " + str(e))

consultaSelect()
