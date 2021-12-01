import gi, GridConBotones, os

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gio


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__(title="Ejemplo de FlowBox")
        self.set_border_width(5)
        self.set_size_request(300, 300)

        self.cabecera = Gtk.HeaderBar(title="Flow Box")
        self.cabecera.set_subtitle("Con cabecera HeaderBar")
        self.cabecera.props.show_close_button = True
        self.set_titlebar(self.cabecera)

        self.boton = Gtk.Button()
        self.icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        self.imaxe = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.BUTTON)
        self.boton.add(self.imaxe)
        self.cabecera.add(self.boton)

        self.caja = Gtk.HBox()
        Gtk.StyleContext.add_class(self.caja.get_style_context(), "linked")

        self.boton2 = Gtk.Button()
        self.boton2.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT, shadow_type=Gtk.ShadowType.NONE)
        )
        self.caja.add(self.boton2)

        self.boton3 = Gtk.Button.new_from_icon_name("pan-end-symbolic", Gtk.IconSize.MENU)
        self.caja.add(self.boton3)
        self.cabecera.pack_start(self.caja)

        self.flowBox = Gtk.FlowBox()
        self.flowBox.set_valign(Gtk.Align.START)
        self.flowBox.set_max_children_per_line(30)
        self.flowBox.set_selection_mode(Gtk.SelectionMode.NONE)

        for i in range(50):
            self.cuadro = GridConBotones.Grid()
            self.flowBox.add(self.cuadro)

        self.barras = Gtk.ScrolledWindow()
        self.barras.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        self.barras.add(self.flowBox)
        self.add(self.barras)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
