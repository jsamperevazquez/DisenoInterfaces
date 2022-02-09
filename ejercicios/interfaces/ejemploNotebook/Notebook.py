import gi
import GridConBotones
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__(title="Ejemplo Notebook")
        self.set_border_width(5)
        self.set_size_request(300, 300)
        self.carpeta = Gtk.Notebook()

        self.pagina1 = Gtk.VBox()
        self.pagina1.set_border_width(10)
        self.pagina1.add(Gtk.Label(label="Página principal"))
        self.carpeta.append_page(self.pagina1, Gtk.Label(label="Identificador de la página"))

        self.pagina2 = Gtk.Notebook()
        self.pagina2.set_border_width(10)
        self.pagina2.add(Gtk.Label(label="Página con icono en la solapa"))
        self.carpeta.append_page(self.pagina2, Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))

        self.caja_con_botones = GridConBotones.Grid()
        self.carpeta.append_page(self.caja_con_botones, Gtk.Label(label="Grid con botones"))

        self.add(self.carpeta)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
