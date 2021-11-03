import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion:

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("saludo.glade")
        self.ventana = builder.get_object("Saludo")
        # Obtengo referencias para interactuar con los objetos:
        self.txtSaludo = builder.get_object("txtNombre")
        self.btnSaludo = builder.get_object("btnSaludo")
        self.lblTexto = builder.get_object("lblTexto")
        # Creamos un diccionario
        senales = {"on_Interface_destroy": Gtk.main_quit,
                   "on_btnSaludo_clicked": self.onBtnSaludoClicked,
                   "on_txtNombre_activate": self.ontxtNombreActivated
                   }

        builder.connect_signals(senales)  # Está a la escucha de las funciones que tengas definidas
        self.ventana.show_all()

    def onBtnSaludoClicked(self, boton):
        self.saludoPersonalizado()

    def ontxtNombreActivated(self, control):
        self.saludoPersonalizado()

    def saludoPersonalizado(self):
        nombre = self.txtSaludo.get_text()
        self.lblTexto.set_text("Hola " + nombre)


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
