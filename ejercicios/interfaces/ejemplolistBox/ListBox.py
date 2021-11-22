import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class ListBoxRowConDatos(Gtk.ListBoxRow):
    def __init__(self, palabra):
        super().__init__()
        self.palabra = palabra
        self.add(Gtk.Label(label=palabra))


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__(title="Ejemplo de listBox")
        self.set_border_width(5)
        self.set_size_request(300, 300)

        self.cajaExterna = Gtk.VBox(spacing=6)
        self.add(self.cajaExterna)

        self.listBox = Gtk.ListBox()
        self.listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.cajaExterna.pack_start(self.listBox, True, True, 0)

        self.fila = Gtk.ListBoxRow()
        self.cajaH = Gtk.HBox(spacing=50)
        self.fila.add(self.cajaH)

        self.cajaV = Gtk.VBox()
        self.cajaH.pack_start(self.cajaV, True, True, 0)

        self.etiqueta = Gtk.Label(label="Fecha y hora", xalign=0)
        self.etiqueta2 = Gtk.Label(label="Requiere acceso a interRed", xalign=0)
        self.cajaV.pack_start(self.etiqueta, True, True, 0)
        self.cajaV.pack_start(self.etiqueta2, True, True, 0)

        self.conmutador = Gtk.Switch()
        self.conmutador.props.valign = Gtk.Align.CENTER
        self.cajaH.pack_start(self.conmutador, True, True, 0)

        self.fila2 = Gtk.ListBoxRow()
        self.cajaH2 = Gtk.HBox(spacing=50)
        self.fila2.add(self.cajaH2)
        self.etiqueta3 = Gtk.Label(label="Permitir actualizaciones automáticas", xalign=0)
        self.chkActualizaciones = Gtk.CheckButton()
        self.cajaH2.pack_start(self.etiqueta3, True, True, 0)
        self.cajaH2.pack_start(self.chkActualizaciones, True, True, 0)

        self.fila3 = Gtk.ListBoxRow()
        self.cajaH3 = Gtk.HBox(spacing=50)
        self.fila3.add(self.cajaH3)
        self.etiqueta4 = Gtk.Label(label="Formato fecha", xalign=0)
        self.cmbFormatoFecha = Gtk.ComboBoxText()
        self.cmbFormatoFecha.insert(0, "0", "24-hour")
        self.cmbFormatoFecha.insert(1, "1", "AM/PM")
        self.cajaH3.pack_start(self.etiqueta4, True, True, 0)
        self.cajaH3.pack_start(self.cmbFormatoFecha, True, True, 0)

        self.listBox2 = Gtk.ListBox()
        self.elementos = "Esta es una lista ordenada para mostrar".split()
        for elemento in self.elementos:
            self.listBox2.add(ListBoxRowConDatos(elemento))

        def ordenar(fila, fila2, datos, notify_destroy):
            return len(fila.palabra) < len(fila2.palabra)  # Nuestra función ordenará por tamaño de las palabras

        def filtrar(fila, datos, notify_destry):
            return False if fila.palabra[
                                len(fila.palabra) - 1] == "a" else True  # Nuestra función filtrará si el último caracter de la palabra es "a"

        self.listBox2.set_sort_func(ordenar, None, False)
        self.listBox2.set_filter_func(filtrar, None, False)
        self.listBox2.connect("row-activated", self.on_row_activated)

        self.cajaExterna.pack_start(self.listBox2, True, True, 0)
        self.listBox2.show_all()

        self.listBox.add(self.fila)
        self.listBox.add(self.fila2)
        self.listBox.add(self.fila3)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_row_activated(self, listBox, fila):
        print(fila.palabra)


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
