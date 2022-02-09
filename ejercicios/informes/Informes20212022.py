from reportlab.pdfgen import canvas

lienzo = canvas.Canvas("documento.pdf")
lienzo.drawString(0, 0, "Posicion incial (x,y)=(0,0)")
lienzo.drawString(50, 100, "Posicion (x,y)=(50,100)")
lienzo.drawString(200, 50, "Posicion (x,y)=(200,50)")

lienzo.drawImage("/home/angel/Escritorio/carpeta.png", 350, 300, 100, 100)


lienzo.showPage()
lienzo.save()