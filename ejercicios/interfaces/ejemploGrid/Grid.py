import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__(title="Ejemplo de Grid")
        self.cuadricula = Gtk.Grid()
        self.add(self.cuadricula)

        self.boton1 = Gtk.Button(label="Boton1")
        self.boton2 = Gtk.Button(label="Boton2")
        self.boton3 = Gtk.Button(label="Boton3")
        self.boton4 = Gtk.Button(label="Boton4")
        self.boton5 = Gtk.Button(label="Boton5")
        self.boton6 = Gtk.Button(label="Boton6")

        self.cuadricula.add(self.boton1)
        self.cuadricula.attach(self.boton2, 1, 0, 2, 1)
        self.cuadricula.attach_next_to(self.boton3, self.boton1, Gtk.PositionType.BOTTOM, 1, 2)
        self.cuadricula.attach(self.boton4, 1, 1, 2, 1)
        self.cuadricula.attach_next_to(self.boton5, self.boton4, Gtk.PositionType.BOTTOM, 1, 1)
        self.cuadricula.attach_next_to(self.boton6, self.boton5, Gtk.PositionType.RIGHT, 1, 1)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
