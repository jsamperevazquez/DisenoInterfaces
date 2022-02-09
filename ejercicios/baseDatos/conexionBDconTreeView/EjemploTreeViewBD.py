import gi
import sqlite3 as dbapi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__()
        self.set_title("Exemplo TreeView conexion a SQLite")
        self.set_border_width(5)
        self.set_default_size(500, 300)

        self.usuarios = Gtk.ListStore(str, str, str)

        try:
            self.bd = dbapi.connect("BD.dat")
            self.cursor = self.bd.cursor()
            self.cursor.execute(f"Select * from usuarios;")
            self.bd.commit()
            for i in self.cursor.fetchall():
                self.usuarios.append([i[0], i[1], i[2]])

        except dbapi.DatabaseError as e:
            print("Error en base de datos: " + str(e))

        grid = Gtk.Grid()
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        trv_vista_users = Gtk.TreeView(model=self.usuarios)
        for i, tituloColumna in enumerate(["D.N.I", "Nombre", "Direccion"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            trv_vista_users.append_column(columna)

        seleccion = trv_vista_users.get_selection()
        seleccion.connect("changed", self.on_trvVista_Users_changed)

        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        grid.attach(scroll, 0, 0, 8, 10)
        scroll.add(trv_vista_users)

        self.dni = Gtk.Entry()
        self.nombre = Gtk.Entry()
        self.direccion = Gtk.Entry()
        self.modificar = Gtk.Button(label="Modificar")
        self.modificar.connect("clicked", self.on_modificar_clicked, seleccion)
        self.modificar.set_sensitive(False)

        grid.attach(self.dni, 0, 10, 2, 1)
        grid.attach_next_to(self.nombre, self.dni, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.direccion, self.nombre, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.modificar, self.direccion, Gtk.PositionType.RIGHT, 2, 1)

        self.add(grid)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_trvVista_Users_changed(self, selec):
        modelo, punteiro = selec.get_selected()
        self.dni.set_text(modelo[punteiro][0])
        self.dni_sql = modelo[punteiro][0]
        self.nombre.set_text(modelo[punteiro][1])
        self.direccion.set_text(modelo[punteiro][2])
        self.modificar.set_sensitive(True)

    def on_modificar_clicked(self, control, seleccion):
        modelo, fila = seleccion.get_selected()
        modelo[fila][0] = self.dni.get_text()
        modelo[fila][1] = self.nombre.get_text()
        modelo[fila][2] = self.direccion.get_text()
        self.cursor.execute(
            f"UPDATE usuarios set dni='{self.dni.get_text()}',nombre='{self.nombre.get_text()}',direccion='{self.direccion.get_text()}' where dni= '{self.dni_sql}'")
        self.bd.commit()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
