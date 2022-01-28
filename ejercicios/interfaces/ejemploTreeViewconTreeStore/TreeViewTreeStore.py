import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo TreeView con TreeStore")
        self.set_border_width(5)

        # Modelo
        modelo = Gtk.TreeStore(str, int, str, bool)
        for abuelo in range(5):
            punteroAbuelo = modelo.append(None, ['Abuelo', abuelo, "Sin datos", True])
            for padre in range(4):
                punteroPadre = modelo.append(punteroAbuelo, ['Padre', padre, "Legítimo", False])
                for Hijo in range(6):
                    punteroHijo = modelo.append(punteroPadre, ['Hijo', Hijo, "Legítimo", True])

        trvArbolGeneralogico = Gtk.TreeView(model=modelo)
        # Columna 1
        trvColumna = Gtk.TreeViewColumn('Parentesco')
        trvArbolGeneralogico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        celda.connect("edited", self.on_columna_edited, modelo)
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 0)
        # Columna 2
        trvColumna = Gtk.TreeViewColumn("Orden")
        trvArbolGeneralogico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 1)
        # Columna 3
        tipoParentesco = Gtk.ListStore(str)
        tipoParentesco.append(["Sin datos"])
        tipoParentesco.append(["Legítimo"])
        tipoParentesco.append(["Bastardo"])

        celdaCombo = Gtk.CellRendererCombo()
        celdaCombo.set_property("editable", True)
        celdaCombo.set_property("model", tipoParentesco)
        celdaCombo.set_property("text-column", 0)
        celdaCombo.set_property("has-entry", False)
        celdaCombo.connect("edited", self.on_combo_edited, modelo)
        trvColumnaCombo = Gtk.TreeViewColumn("Combo", celdaCombo, text=2)
        trvArbolGeneralogico.append_column(trvColumnaCombo)
        # Columna 4
        trvColumna = Gtk.TreeViewColumn("Vivo")
        celda = Gtk.CellRendererToggle()
        celda.set_property("activatable", True)
        celda.connect("toggled", self.on_check_toggled, modelo)
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "active", 3)
        trvArbolGeneralogico.append_column(trvColumna)

        self.add(trvArbolGeneralogico)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_combo_edited(self, control, fila, texto, modelo):
        modelo[fila][2] = texto

    def on_columna_edited(self, control, fila, texto, modelo):
        modelo[fila][0] = texto

    def on_check_toggled(self, control, fila, modelo):
        modelo[fila][3] = not modelo[fila][3]


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
