import os.path

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

elementos = []

hojaEstilo = getSampleStyleSheet()

cabecera = hojaEstilo["Heading4"]
cabecera.pageBreakeBefore = 5  # no hay cabecera porque está a 0
cabecera.keepWithNext = 0  # empezar con la primera pagina en blanco (no = 0)
cabecera.backColor = colors.aliceblue
parrafo = Paragraph("CABECERA DEL DOCUMENTO", cabecera)
elementos.append(parrafo)

cadena = "Ejemplo de utilización de ReportLab con Platypus" * 500
cuerpo = hojaEstilo["BodyText"]
parrafo2 = Paragraph(cadena, cuerpo)
elementos.append(parrafo2)
elementos.append(Spacer(0, 20, True))

logo = Image(os.path.realpath("/home/angel/Imágenes/agarimoLogo.png"), 500, 150)
elementos.append(logo)

doc = SimpleDocTemplate("ejemploPlatypus.pdf", pagesize=A4, showBoundary=1)
doc.build(elementos)