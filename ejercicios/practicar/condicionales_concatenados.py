print("Evaluación de salarios")

salario_presidente=int(input("introduce salario presidente\n"))
print("salario presidente: " + str(salario_presidente)) #Con la función str convertimos el entero en cadena de texo, pues no es posible concatenarlos en python


salario_director=int(input("introduce salario director\n"))
print("salario director: " + str(salario_director))


salario_jefe_area=int(input("introduce salario jefe area\n"))
print("salario salario_jefe_area: " + str(salario_jefe_area))

salario_administrativo=int(input("introduce salario administrativo\n"))
print("salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:# Si alguno de ellos no cumple de izquierda a derecha entrará en else
	print("todo funciona correctamente")
else:
	print("algo falla en esta empresa")
