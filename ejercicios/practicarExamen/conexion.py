import sqlite3
import sqlite3 as dbapi
from sqlite3 import connect
from sqlite3 import Error


class conexionBD:

    def __init__(self, rutaBd):

        self.rutaBd = rutaBd
        self.conexion = None
        self.cursor = None

    def conectBD(self):

        try:
            if self.conexion is None:
                if self.rutaBd is None:
                    print("La ruta de la base es Nula")

                else:
                    self.conexion = connect(self.rutaBd)
            else:
                print("Base de datos conectada: " + self.conexion)
        except Error as e:
            print("Error en la conexión a la base de datos. Error: ".__add__(str(e)))

        else:
            print("Conexión establecida")

    def crearCursor(self):
        try:
            if self.conexion is None:
                print("Para crear cursor es necesaria conexion a BD")
            else:
                if self.cursor is None:
                    self.cursor = self.conexion.cursor()  # OJO no completa el .cursor()
                else:
                    print("El cursor ya esta en uso")
        except Error as e:
            print(e)
        else:
            print("Cursor preparado")

    def consultarParametros(self, consultaSQL):

        lisaConsulta = list()

        try:
            if self.conexion is None:
                print("Conexion requerida")
            else:
                if self.cursor is None:
                    print("Cursor requerido")
                else:
                    self.cursor.execute(consultaSQL)

                    for fila in self.cursor.fetchall():
                        lisaConsulta.append(fila)
        except sqlite3.DatabaseError as e:
            print(e)
            return None
        else:
            print("Consulta ejecutada")
            return lisaConsulta

    def consultarParametros(self, consultaSQL, *parametros):
        lista_consulta = list()
        try:
            if self.conexion is None:
                print("Conexion requerida")
            else:
                if self.cursor is None:
                    print("Cursor requerido")
                else:
                    self.cursor.execute(consultaSQL, parametros)
                    for fila in self.cursor.fetchall():
                        lista_consulta.append(fila)

        except dbapi.DatabaseError as e:
            print("Error en consulta ".__add__(str(e)))
            return None
        else:
            print("Consulta realizada")
            return lista_consulta
