import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf

class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo ComboBox")
        self.set_border_width(5)

        modelo = Gtk.ListStore (int, str)
        modelo.append ([1, "Manuel"])
        modelo.append([2, "Angel"])
        modelo.append([3, "Marcos"])
        modelo.append([19, "Alexander"])
        modelo.append([8, "Joel"])
        modelo.append([4, "Britza"])

        caixaV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing=6)

        cmbNomes = Gtk.ComboBox.new_with_model_and_entry(modelo)
        cmbNomes.connect ("changed", self.on_cmbNomes_changed)
        cmbNomes.set_entry_text_column(1)
        cmbNomesEntry = cmbNomes.get_child()
        cmbNomesEntry.connect("activate", self.on_cmbNomesEntry_activate,modelo)
        #celda = Gtk.CellRendererText()
        #cmbNomes.pack_start(celda,True)
        #cmbNomes.add_attribute(celda, "text", 1)
        caixaV.pack_start (cmbNomes, False, False,0)

        mdlPaises = Gtk.ListStore (str)
        paises = ["Letonia","Brasil", "Arxentina", "Surinam", "Kenia", "Islandia", "Xapón"]
        for pais in paises:
           mdlPaises.append([pais])

        cmbPaises = Gtk.ComboBox.new_with_model(mdlPaises)
        cmbPaises.connect ("changed", self.on_cmbPaises_changed)
        celda = Gtk.CellRendererText()
        cmbPaises.pack_start(celda, True)
        cmbPaises.add_attribute (celda, "text", 0)
        caixaV.pack_start (cmbPaises,True, True, 10)

        mdlImaxes = Gtk.ListStore(str, str)
        imaxes = [("Cortar","edit-cut"),
                  ("pegar","edit-paste"),
                  ("Copiar", "edit-copy"),
                  ("Novo", "document-new"),
                  ("Abrir", "document-open"),
                  ("Gardar", "document-save")]
        for etiqueta, imaxe in imaxes:
            mdlImaxes.append ([etiqueta,imaxe])

        cmbImaxes = Gtk.ComboBox.new_with_model(mdlImaxes)
        celda = Gtk.CellRendererText()
        cmbImaxes.pack_start(celda, True)
        cmbImaxes.add_attribute(celda, "text", 0)
        caixaV.pack_start(cmbImaxes, True, True, 10)

        trvImaxes = Gtk.TreeView ()
        trvImaxes.set_model (mdlImaxes)
        celdaTexto = Gtk.CellRendererText()
        columnaTexto = Gtk.TreeViewColumn("Texto", celdaTexto, text=0)
        trvImaxes.append_column(columnaTexto)
        celdaImaxes = Gtk.CellRendererPixbuf()
        columnaImaxes = Gtk.TreeViewColumn ("Imaxe", celdaImaxes, icon_name=1)
        trvImaxes.append_column(columnaImaxes)
        caixaV.pack_start (trvImaxes, True, False, 5)


        self.add (caixaV)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_cmbNomes_changed (self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            id_fila, nome = modelo [fila][:2]
            idFila = modelo [fila][0]
            nome2 = modelo [fila][1]
            print ("Seleccionado: ID=%d, nome=%s" % (id_fila, nome))
        #else:
            #cadroTexto = combo.get_child()
            #print ("Escrito: %s"% cadroTexto.get_text())

    def on_cmbNomesEntry_activate(self, cadroTexto, modelo):
        print("Escrito: %s" % cadroTexto.get_text())
        modelo.append([10, cadroTexto.get_text()])

    def on_cmbPaises_changed (self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            pais = modelo [fila][0]
            print ("Pais seleccionado: %s" % pais)


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()