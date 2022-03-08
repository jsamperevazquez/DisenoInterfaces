import gi
import ejercicios.examen2Evaluacion.Conexion
import ejercicios.examen2Modulado.Modelo.Ventas
from gi.repository import Gtk, Gio

gi.require_version("GTK", "3.0")


class Aplicacion(Gtk.Window):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.set_title("Examen")
        self.set_border_width(5)
        self.set_default_size(300, 250)

        caja_V = Gtk.VBox()
        caja_H = Gtk.HBox()

        lbl_numero_albaran = Gtk.Label(label="Numero de albarán")
        caja_H.pack_start(lbl_numero_albaran, False, False, 2)

        modeloNumeroAlbaran = Gtk.ListStore(int)

        bd = ejercicios.examen2Evaluacion.Conexion.ConexionBD("Datos/modelosClasicos.dat")
        bd.cursor()
        bd.creaCursor()

        numero_albaran = list(ejercicios.examen2Modulado.Modelo.Ventas)



