print ("Control de acceso")

edad_usuario=int(input("porfavor introduzca su edad\n"))
if edad_usuario in range(0,17):# in range es un rango de valores, en este caso de 0 a 17
	print("No puedes pasar gilipollas")
elif edad_usuario>100 or edad_usuario <0: #elif tiene que ir siempre después de if para que el else coja todo el bloque (if y elif),
	print ("Edad no valida")
else:
	print("Adelante mamagaitas")



