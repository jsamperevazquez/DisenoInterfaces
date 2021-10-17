import math 


def calculaRaiz(num1):
	
	
	if num1<0:
		raise ValueError ("El número no puede ser negativo") # Lanzamos una excepción para que rompa

	else:
		return math.sqrt(num1)


op1=int(input("introduce un número: \n"))

try:
	print (calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo: #Le damos un alias a ese error para poder imprimir el mensaje.
	print(ErrorDeNumeroNegativo) #Imprime el mensaje que le hemos dado al error ("el numero no puede ser negativo")

print("programa terminado")
