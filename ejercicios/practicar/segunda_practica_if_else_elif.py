print("notas de alumno")

nota_alumno=float(input("introduce la nota del alumno"))

if nota_alumno <5 and nota_alumno>0:
	print("El alumno está suspenso")
elif nota_alumno >10 or nota_alumno <0:
	print ("nota invalida")
else:
	print("El alumno está aprobado")