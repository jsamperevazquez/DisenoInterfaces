import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class Grid(Gtk.Grid):
    def __init__(self):
        super(Grid, self).__init__()

        self.boton1 = Gtk.Button(label="Boton1")
        self.boton2 = Gtk.Button(label="Boton2")
        self.boton3 = Gtk.Button(label="Boton3")
        self.boton4 = Gtk.Button(label="Boton4")
        self.boton5 = Gtk.Button(label="Boton5")
        self.boton6 = Gtk.Button(label="Boton6")

        self.add(self.boton1)
        self.attach(self.boton2, 1, 0, 2, 1)
        self.attach_next_to(self.boton3, self.boton1, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach(self.boton4, 1, 1, 2, 1)
        self.attach_next_to(self.boton5, self.boton4, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(self.boton6, self.boton5, Gtk.PositionType.RIGHT, 1, 1)