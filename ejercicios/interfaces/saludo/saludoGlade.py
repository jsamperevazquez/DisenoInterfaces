import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion:

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("saludo.glade")

        self.ventana = builder.get_object("Saludo")
        self.ventana.show_all()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()

