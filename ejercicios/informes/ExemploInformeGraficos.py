from reportlab.platypus import SimpleDocTemplate
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.charts.piecharts import Pie
from reportlab.platypus import Spacer
from reportlab.graphics.charts.legends import Legend

guion = []

d = Drawing(200, 50)
etiqueta = Label()
etiqueta.fontName = 'Helvetica'
etiqueta.setOrigin(100, 40)
etiqueta.angle = 45
etiqueta.dx = 0
etiqueta.dy = -20
etiqueta.boxStrokeColor = colors.green
etiqueta.setText('Ventas \n ano \n 2021')
d.add(etiqueta)
guion.append(d)

d = Drawing(400, 200)

datos = [(23, 14, 10, 9, 19, 21, 25, 4),
         (2, 7, 9, 16, 14, 19, 20, 24)]

bg = VerticalBarChart()
bg.data = datos
bg.x = 50
bg.y = 50
bg.height = 125
bg.width = 300
bg.strokeColor = colors.grey
bg.valueAxis.valueMin = 0
bg.valueAxis.valueMax = 30
bg.valueAxis.valueStep = 10
bg.valueAxis.labels.fontName = 'Helvetica'
bg.categoryAxis.labels.boxAnchor = 'ne'  # North east
bg.categoryAxis.labels.dx = 8
bg.categoryAxis.labels.dy = -2
bg.categoryAxis.labels.angle = 30
bg.categoryAxis.categoryNames = ['Xan-21', 'Feb-21', 'Mar-21', 'Abr-21', 'Mai-21', 'Xun-21', 'Xul-21', 'Ago-21']
bg.groupSpacing = 10
bg.barSpacing = 2
bg.bars[0].fillColor = colors.yellowgreen
bg.bars[1].fillColor = colors.greenyellow
bg.bars[1].strokeColor = colors.yellow
bg.bars[0].strokeColor = colors.green
d.add(bg)
guion.append(d)

guion.append(Spacer(0, 30))

# Creamos area de dibujo
d2 = Drawing(300, 200)

tarta = Pie()
tarta.data = [3, 12, 15, 50, 30]
tarta.labels = ["No Presentados", "Suspensos", "Aprobados", "Notables", "Sobresalientes"]
tarta.x = 65
tarta.y = 15
tarta.width = 180
tarta.height = 180

# Ancho de la linea de contorno de porción
tarta.slices.strokeWidth = 0.5
# Resaltamos la porción 3
tarta.slices[2].popout = 10  # Separa la porción
tarta.slices[3].strokeWidth = 2
tarta.slices[3].strokeDashArray = [2, 2]
tarta.slices[3].fontColor = colors.red

# Ponemos lineas a etiquetas
tarta.sideLabels = 1

d2.add(tarta)
leyenda = Legend()
leyenda.x = 370
leyenda.y = 0
leyenda.dx = 8
leyenda.dy = 8
leyenda.fontName = "Helvetica"
leyenda.fontSize = 7
leyenda.boxAnchor = "n"
leyenda.columnMaximum = 10
leyenda.strokeColor = 1
leyenda.strokeColor = colors.black
leyenda.autoXPadding = 5
leyenda.yGap = 0
leyenda.dxTextSpace = 5
leyenda.alignment = "right"
leyenda.dividerLines = 1 | 2 | 4
leyenda.dividerOffsY = 4.5
leyenda.subCols.rpad = 30

colores = [colors.pink, colors.red, colors.green, colors.blue, colors.yellow]

for i, color in enumerate(colores):
    tarta.slices[i].fillcolor = color

leyenda.colorNamePairs = [(tarta.slices[i].fillcolor,
                           (tarta.labels[i][0:20], "%0.2f" % tarta.data[i]))
                            for i in range(len(tarta.data))]

d2.add(leyenda)
guion.append(d2)

guion.append(Spacer(0, 30))

doc = SimpleDocTemplate("informeGraficos.pdf", pagesize=A4)
doc.build(guion)
