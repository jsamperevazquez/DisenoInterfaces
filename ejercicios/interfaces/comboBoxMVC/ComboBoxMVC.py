import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo FlowBox")
        self.set_border_width(5)
        self.set_size_request(300, 250)

        modelo = Gtk.ListStore(int, str)  # Le tenemos que decir que tipo de dato para cada columna
        modelo.append([1, "Manuel"])  # Añadir campos
        modelo.append([2, "Angel"])  # Añadir campos
        modelo.append([3, "Pepe"])  # Añadir campos
        modelo.append([4, "Francisco"])  # Añadir campos
        modelo.append([5, "CristobalColon"])  # Añadir campos
        modelo.append([6, "Pimpinela"])  # Añadir campos
        modelo.append([7, "Mateo"])  # Añadir campos
        modelo.append([8, "Marianico"])  # Añadir campos

        cajaV = Gtk.VBox(spacing=6)
        cmbNombres = Gtk.ComboBox.new_with_model_and_entry(modelo)
        cmbNombres.connect("changed", self.on_cmbNombres_changed)
        cmbNombres.set_entry_text_column(1)  # Nos muestra el dato de la columna dada

        cmbNombresEntry = cmbNombres.get_child()
        cmbNombresEntry.connect("activate", self.on_cmbNombresEntry_activate, modelo)

        # celda = Gtk.CellRendererText()
        # cmbNombres.pack_start(celda, True)
        # cmbNombres.add_attribute(celda, "text", 1)
        cajaV.pack_start(cmbNombres, False, False, 0)

        self.add(cajaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_cmbNombres_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()  # Obtenemos la referencia al modelo
            id_fila, nombre = modelo[fila][:2]
            print("Seleccionado: ID=%d, nombre=%s" % (id_fila, nombre))
        # else:
        # cuadroTexto = combo.get_child()
        # print("Escrito: %s" % cuadroTexto.get_text())

    def on_cmbNombresEntry_activate(self, cuadroTexto, modelo):
        print("Escrito: %s" % cuadroTexto.get_text())
        modelo.append([23, cuadroTexto.get_text()])


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()

# TODO hacer inserciones en la base de datos del ejemplo Conexión