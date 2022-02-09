print ("programa de evaluacion de alumnos")

nota_alumno=int(input("Introduce la nota del alumno"'\n'))#Con input() pedimos valar por pantalla.Si vamos a manejar valores numéricos tenemos que indicarlo con la función int(),por defecto el input solo recibe texto
if nota_alumno >10 or nota_alumno<0: #doble condición para que los valores que se introduzcan sean correctos
	print("nota no valida")
else:
	def evaluacion(nota): #Creo una función para analizar la nota en caso de que los parámetros introducidos sean correctos
		evaluacion="Aprobado" # Esta variable solo tiene valor dentro de la función, fuera no existe (dentro del ámbito)
		if nota <5:
			evaluacion="suspenso"
		return(evaluacion) # me retorna el valor de la función
	print(evaluacion(nota_alumno))# El valor que le demos en nota_alumno se almacena dentro de la función en nota.

		


