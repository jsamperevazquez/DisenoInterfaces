import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__(title="Ejemplo de un Gtk.label")
        self.set_size_request(200, 150)
        self.temporizador = None

        self.cajaV = Gtk.VBox(spacing=8)
        self.add(self.cajaV)
        self.txtTexto = Gtk.Entry()
        self.txtTexto.set_width_chars(30)
        self.txtTexto.set_text("Bienvenidos")
        self.cajaV.pack_start(self.txtTexto, True, True, 0)

        self.cajaH = Gtk.HBox(spacing=8)
        self.cajaV.pack_start(self.cajaH, True, True, 0)

        self.chkEditable = Gtk.CheckButton(label="Editable")
        self.chkEditable.connect("toggled", self.on_chkEditable_toggled)
        self.chkEditable.set_active(True)

        self.cajaH.pack_start(self.chkEditable, True, True, 0)

        self.chkVisible = Gtk.CheckButton(label="Visible")
        self.chkVisible.connect("toggled", self.on_chkVisible_toggled)
        self.chkVisible.set_active(True)

        self.cajaH.pack_start(self.chkVisible, True, True, 0)

        self.chkPulso = Gtk.CheckButton(label="Pulso")
        self.chkPulso.connect("toggled", self.on_chkPulso_toggled)
        self.chkPulso.set_active(True)

        self.cajaH.pack_start(self.chkPulso, True, True, 0)

        self.chkIcono = Gtk.CheckButton(label="Icono")
        self.chkIcono.connect("toggled", self.on_chkIcono_toggled)
        self.chkIcono.set_active(True)

        self.cajaH.pack_start(self.chkIcono, True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_chkEditable_toggled(self, control):
        estado = control.get_active()
        self.txtTexto.set_editable(estado)

    def on_chkVisible_toggled(self, control):
        estado = control.get_active()
        self.txtTexto.set_visible(estado)

    def on_chkPulso_toggled(self, control):
        if control.get_active():
            self.txtTexto.set_progress_pulse_step(0.5)
            self.temporizador = GLib.timeout_add(300, self.hacer_pulso, None)
        else:
            GLib.source_remove(self.hacer_pulso)
            self.temporizador = None
            self.txtTexto.set_progress_pulse_step(0)

    def hacer_pulso(self, datosUsuario):
        self.txtTexto.progress_pulse()
        return True

    def on_chkIcono_toggled(self, control):
        if control.get_active():
            nombre_icono = "system-error-symbolic"
        else:
            nombre_icono = None
        self.txtTexto.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, nombre_icono)


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
