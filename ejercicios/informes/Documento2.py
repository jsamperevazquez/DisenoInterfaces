from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

operaciones = []
# Creas la imagen:
imagen = Image(400, 0, 100, 100, "/home/angel/Escritorio/carpeta.png")
# Creas el dibujo (contenedor)
dibujo = Drawing(30, 30)
dibujo.add(imagen)
dibujo.translate(0, 500)

operaciones.append(dibujo)

dibujo = Drawing(30, 30)
dibujo.add(imagen)
dibujo.rotate(45) # Se rota 45º
dibujo.scale(1.5, 0.5) #Reescalamos imagen
dibujo.translate(-30, 200) #Trasdadas imagen
operaciones.append(dibujo)

dibbujo = Drawing(A4[0], A4[1])
for operacion in operaciones:
    dibbujo.add(operacion)

renderPDF.drawToFile(dibbujo, "documento2.pdf")

