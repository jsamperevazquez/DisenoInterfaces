import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__(title="MAYUSCULAS o minusculas")
        self.set_size_request(300, 150)
        self.caja = Gtk.VBox(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.caja)
        self.caja_h = Gtk.VBox(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.entry = Gtk.Entry().new()
        self.caja.pack_start(self.entry, True, True, 0)
        self.caja.pack_end(self.caja_h, True, True, 0)
        self.boton_mayus = Gtk.Button(label="MAYUS")
        self.boton_minus = Gtk.Button(label="minus")
        self.caja_h.pack_start(self.boton_mayus, True, True, 0)
        self.caja_h.pack_start(self.boton_minus, True, True, 0)
        self.boton_mayus.connect("clicked", self.on_boton_may_clicked)
        self.boton_minus.connect("clicked", self.on_boton_min_clicked)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def on_boton_may_clicked(self, boton):
        contenido = str.upper(self.entry.get_text())
        self.entry.set_text(contenido)

    def on_boton_min_clicked(self, boton):
        contenido = str.lower(self.entry.get_text())
        self.entry.set_text(contenido)


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
