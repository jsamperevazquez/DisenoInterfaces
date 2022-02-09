import gi
import os

import gtk

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gio, Gdk


class AddElement(Gtk.HBox):
    def __init__(self, fichero):
        super().__init__()
        self.set_homogeneous(True)
        self.fichero = fichero
        self.imagen_archivo = Gtk.Image.new_from_file(
            "/home/angel/Escritorio"
            "/fileinterfacesymboloftextpapersheet_79740.png")
        self.imagen_directorio = Gtk.Image.new_from_file("/home/angel/Escritorio/carpeta.png")

        if fichero.is_file():
            self.add(Gtk.Label(label=fichero.name))
            self.add(self.imagen_archivo)
        elif fichero.is_dir():
            self.add(Gtk.Label(label=fichero.name))
            self.add(self.imagen_directorio)


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__(title="Apliclacion flowBox")
        self.set_border_width(5)
        self.set_size_request(700, 500)
        self.cabecera = Gtk.HeaderBar(title="Mostrar contenido")
        self.cabecera.set_subtitle("Listar archivos y directorios")
        self.cabecera.set_show_close_button(True)
        self.set_titlebar(self.cabecera)

        self.cajaExterna = Gtk.VBox(spacing=5)
        self.cajaHorizontal = Gtk.HBox(spacing=5)
        self.cajaExterna.pack_start(self.cajaHorizontal, True, True, 0)

        self.etiqueta = Gtk.Label()

        self.boton1 = Gtk.Button()
        self.boton2 = Gtk.Button()
        self.icon = Gio.ThemedIcon(name="search-symbolic")
        # self.imaxe = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.BUTTON)
        # self.boton.add(self.imaxe)
        self.boton1.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT, shadow_type=Gtk.ShadowType.NONE)
        )
        self.boton2.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.RIGHT, shadow_type=Gtk.ShadowType.NONE)
        )
        self.cabecera.add(self.boton1)
        self.cabecera.add(self.boton2)

        self.entry = Gtk.Entry()
        self.entry.set_icon_from_gicon(Gtk.PositionType.LEFT, self.icon)
        self.entry.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.5, 0.5, 1.0, 1.1))
        self.entry.connect("event", self.on_entry_clicked)
        self.entry.set_text("Buscar")
        self.bandera = True  # Flag para que me borre el texto del entry solo la primera vez
        self.entry.new()
        self.cabecera.add(self.entry)

        self.list_box = Gtk.FlowBox()
        self.list_box.set_max_children_per_line(10)

        self.barras = Gtk.ScrolledWindow()
        self.barras.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        self.barras.add(self.list_box)
        self.add(self.barras)

        self.valores_fichero = []
        self.directorio = '/home/angel'
        with os.scandir(self.directorio) as self.contenido:
            for self.fichero in self.contenido:
                self.valores_fichero.append(self.fichero)
                self.list_box.add(AddElement(self.fichero))

        self.cajaHorizontal.pack_start(self.list_box, True, True, 0)

        self.add(self.cajaExterna)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_entry_clicked(self, widget, event, data=None):
        if self.bandera:
            self.entry.set_text("")
            self.bandera = False
        contenido_entry = self.entry.get_text()
        for elemento in self.valores_fichero:
            if contenido_entry == elemento.name:
                #TODO
                print("funciona")


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
