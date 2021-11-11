import numbers

import gi
import gtk

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import Gdk


class Aplication(Gtk.Window):

    def __init__(self):
        super(Aplication, self).__init__(title="Ventana botones")
        self.caja = Gtk.VBox(orientation=Gtk.Orientation.HORIZONTAL)
        self.set_size_request(300, 80)
        self.color_entry = Gtk.Entry.new()
        # Doy nombre al entry para tratarlo en css
        self.color_entry.set_name("color_entry")
        self.text_lab = Gtk.Label.new("  Selecciona color")
        self.caja.pack_start(self.color_entry, True, True, 0)
        self.caja.pack_start(self.text_lab, True, True, 0)

        self.boton1 = Gtk.Button.new_with_label(label="Azul")
        self.boton2 = Gtk.Button.new_with_label(label="rojo")
        self.boton3 = Gtk.Button.new_with_label(label="verde")
        self.caja.pack_start(self.boton1, True, True, 30)
        self.caja.pack_start(self.boton2, True, True, 30)
        self.caja.pack_start(self.boton3, True, True, 30)
        self.boton1.connect("clicked", self.on_botona_clicked)
        self.boton2.connect("clicked", self.on_botonr_clicked)
        self.boton3.connect("clicked", self.on_botonv_clicked)

        self.add(self.caja)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    # Métodos para los botones
    def on_botona_clicked(self, boton):
        provider = Gtk.CssProvider() # Proveedor de css para estilo
        css = """#color_entry { background-image: linear-gradient(blue); }""" # css a mi entry
        provider.load_from_data((css.encode())) # cargo css
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def on_botonr_clicked(self, boton):
        provider = Gtk.CssProvider()
        css = """#color_entry { background-image: linear-gradient(red); }"""
        provider.load_from_data((css.encode()))
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def on_botonv_clicked(self, boton):
        provider = Gtk.CssProvider()
        css = """#color_entry { background-image: linear-gradient(green); }"""
        provider.load_from_data((css.encode()))
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


if __name__ == "__main__":
    Aplication()
    Gtk.main()
