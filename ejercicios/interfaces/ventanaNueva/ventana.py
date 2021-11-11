import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion(Gtk.Window):

    def __init__(self):
        self.contador = 0
        super(Aplicacion, self).__init__(title="Ejemplo de uso de GTK.Label")
        caja_h = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajav_derecha = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        cajav_izquierda = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        caja_h.pack_start(cajav_izquierda, True, True, 0)
        caja_h.pack_start(cajav_derecha, True, True, 0)

        self.etiqueta = Gtk.Label(label='Etiqueta normal')
        cajav_izquierda.pack_start(self.etiqueta, True, True, 0)

        etiqueta2 = Gtk.Label(label="Etiqueta con texto justificado a la izquierda. \n Con múltiples lineas")
        etiqueta2.set_justify(Gtk.Justification.LEFT)
        cajav_izquierda.pack_start(etiqueta2, True, True, 0)

        etiqueta3 = Gtk.Label(label="En este caso es una etiqueta line-wraped\n"
                                    "Esta el texto no no entra en el ancho, ponemos\n "
                                    "varias cadenas de texto que van a ser unidas \n"
                                    "Esto permite múltiples párrafos y añade     espacios extra")
        etiqueta3.set_line_wrap(True)
        etiqueta3.set_max_width_chars(32)
        etiqueta3.set_justify(Gtk.Justification.RIGHT)
        cajav_derecha.pack_start(etiqueta3, True, True, 0)
        # Uso de line_wrap
        etiqueta4 = Gtk.Label(label="En este caso es una etiqueta line-wraped\n"
                                    "Esta el texto no no entra en el ancho, ponemos\n "
                                    "varias cadenas de texto que van a ser unidas \n"
                                    "Esto permite múltiples párrafos y añade     espacios extra\n"
                                    "Párrafo extra largo para hacer más texto")
        etiqueta4.set_line_wrap(True)
        etiqueta4.set_justify(Gtk.Justification.FILL)
        etiqueta4.set_max_width_chars(32)
        cajav_derecha.pack_start(etiqueta4, True, True, 0)

        # Uso de etiquetas <>
        etiqueta5 = Gtk.Label()
        etiqueta5.set_markup("El texto puede tener <small> pequeño </small>, <big> grande </big>,"
                             "<b> negrita </b>, <i> cursiva </i>, y apuntar cara a "
                             '<a href="https://www.gtk.org"'
                             'title="Pulsa para saber más">interrede </a>')
        etiqueta5.set_max_width_chars(48)
        cajav_derecha.pack_start(etiqueta5, True, True, 0)

        etiqueta6 = Gtk.Label.new_with_mnemonic("_Press Alt + P para seleecionar el botón derecho")
        etiqueta6.set_sensitive(True)
        cajav_derecha.pack_start(etiqueta6, True, True, 0)
        # Se
        boton = Gtk.Button(label="Pulsa...")
        boton.connect("clicked", self.on_click)
        etiqueta6.set_mnemonic_widget(boton)
        cajav_derecha.pack_start(boton, True, True, 0)
        self.add(caja_h)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_click(self, boton):
        self.contador += 1
        self.etiqueta.set_text("Numero de pulsaciones " + str(self.contador))
        print("Hola")
        return self.contador


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
