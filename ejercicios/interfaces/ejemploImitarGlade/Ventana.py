import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__(title="Imitar Glade")
        self.set_size_request(450, 100)
        self.grid = Gtk.Grid()

        self.etiqueta = Gtk.Label()
        self.etiqueta.set_markup("<b>Label behaviour</b>")
        self.etiqueta.props.xalign = 0

        self.grid.attach(self.etiqueta, 0, 0, 1, 1)

        self.boton1 = Gtk.CheckButton(label="Seleccionable")
        self.grid.attach_next_to(self.boton1, self.etiqueta, Gtk.PositionType.BOTTOM, 1, 1)

        self.boton2 = Gtk.CheckButton(label="Utilizar subrayado")
        self.grid.attach_next_to(self.boton2, self.boton1, Gtk.PositionType.BOTTOM, 1, 1)

        self.boton3 = Gtk.CheckButton(label="Seguir los enlaces visitados")
        self.grid.attach_next_to(self.boton3, self.boton1, Gtk.PositionType.RIGHT, 1, 1)

        self.entry = Gtk.Entry()
        self.grid.attach_next_to(self.entry, self.boton2,Gtk.PositionType.RIGHT, 1, 1)

        self.add(self.grid)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
