import gi
import GridConBotones

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__(title="Ejemplo de Stack")
        self.set_border_width(5)
        self.set_size_request(300, 300)

        self.cajaV = Gtk.VBox(spacing=5)
        self.add(self.cajaV)

        self.panel = Gtk.Stack()
        self.panel.set_transition_type(Gtk.StackTransitionType.SLIDE_UP)
        self.panel.set_transition_duration(1000)

        self.pulsame = Gtk.CheckButton(label="Púlsame")
        self.panel.add_titled(self.pulsame, "Pulsame", "Pulsa")

        self.etiqueta = Gtk.Label()
        self.etiqueta.set_markup("<big>Una etiqueta presuntuosa</big>")
        self.panel.add_titled(self.etiqueta, "Etiqueta", "Una etiqueta")

        self.caja_botones = GridConBotones.Grid()
        self.caja_botones.set_border_width(10)
        self.panel.add_titled(self.caja_botones, "CajaBotones", "Caja con botones")

        self.selector_paneles = Gtk.StackSwitcher()
        self.selector_paneles.set_stack(self.panel)

        self.cajaV.pack_start(self.selector_paneles, True, True, 0)
        self.cajaV.pack_start(self.panel, True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
