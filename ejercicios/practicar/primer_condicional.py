def evaluacion(nota):
	evaluacion="Aprobado"
	if nota <5:
		evaluacion="suspenso"
	return(evaluacion)

print(evaluacion(3))

		


