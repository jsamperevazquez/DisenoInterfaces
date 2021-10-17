"""Lanzamiento de excepciones
Instrucción RAISE
Creacción de excepciones propias
"""
edad=int(input("introduce la edad:\n"))
def evaluaEdad(edad):
	
	if edad<0:
		raise TypeError("No se permiten edades negativas") # con este raise hacemos un lanzamiento de excepción para que el programa rompa(podemos elegir la que queramos, no tiene porqué ser el error que sea)
		#Podriamos elegir otro (Imprime el mensaje que le pongamos)
	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	elif edad<100:
		return "cuídate"

print (evaluaEdad(edad))


