contador=1
while contador<=10: #mientras el contador sea menor o igual que 10 entrará en el bucle	
	print ("Ejecución " + str(contador)) #Concatenamos el nuestro string con el valor del contador
	contador=contador+1 #sumamos uno a nuestro contador
print("Fin de Ejecución") 

edad=int(input("Introduce la edad \n"))

while edad <0 or edad >100:
	print("la edad " + str(edad) + " es una edad incorrecta ")
	print("Vuelve a intertarlo  \n")
	edad=int(input("Introduce la edad: \n"))
else:
	print("Edad correcta")


