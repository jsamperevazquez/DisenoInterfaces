import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

ventana = Gtk.Window()
ventana.show()
ventana.connect("destroy", Gtk.main_quit)
Gtk.main()