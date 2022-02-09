import gi
import gtk

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__(title="Colores texto")
        self.set_size_request(200, 100)
        self.caja = Gtk.VBox(orientation=Gtk.Orientation.VERTICAL)
        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(10)
        self.caja.pack_end(self.grid, True, True, 0)
        self.boton1 = Gtk.Button("Azul")
        self.boton2 = Gtk.Button("Rojo")
        self.boton3 = Gtk.Button("Verde")
        self.boton1.set_name("boton1")
        self.boton2.set_name("boton2")
        self.boton3.set_name("boton3")
        self.css = """ #boton1 {background-image : linear-gradient(blue);}
                       #boton2 {background-image : linear-gradient(red);}
                       #boton3 {background-image : linear-gradient(green);}"""
        self.boton1.connect("clicked", self.on_botona_clicked)
        self.boton2.connect("clicked", self.on_botonr_clicked)
        self.boton3.connect("clicked", self.on_botonv_clicked)
        self.grid.attach(self.boton1, 2, 0, 2, 1)
        self.grid.attach_next_to(self.boton2, self.boton1, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.boton3, self.boton2, Gtk.PositionType.RIGHT, 1, 1)
        self.etiqueta = Gtk.Label.new("  Selecciona color texto   ")
        self.caja.pack_start(self.etiqueta, True, True, 0)
        self.provider = Gtk.CssProvider()
        self.provider.load_from_data(self.css.encode())
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), self.provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.add(self.caja)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def on_botona_clicked(self, boton):
        self.etiqueta.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.0, 0.0, 1.0, 1.0))

    def on_botonr_clicked(self, boton):
        self.etiqueta.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1.0, 0.0, 0.0, 1.0))

    def on_botonv_clicked(self, boton):
        self.etiqueta.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.0, 1.0, 0.0, 1.0))


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
