import math # importamos las funciones matemáticas de math 
print("Programa de cálculo de raiz cruadada")

numero=int(input("Introduce un numero:  "))

intentos=0 # iniciamos los intentos en 0

while numero<0: # mientras numero es menor a 0 entra en el bucle while 
	print("no se puede hayar la raiz de un numero negativo")

	if intentos==2: #Si intentos vale 2 el while romperá (tres intentos)
		print("Has consumido demasiados intentos, el Programa ha finalizado")
		break; # orden para romper el bucle While, ejecutará las ordenes de después del while.

	numero=int(input("Introduce un numero:  "))
	if numero<0:
		intentos=intentos+1

if intentos<2:# si los intentos son menos de 3 (parte de 0) entra en el if
	solucion=math.sqrt(numero)# la funcion sqrt de math es para hayar la raiz cuadrada
	print("la raiz cruadada de  " + str(numero) + " es " + str(solucion)) # concatenamos el resultado 


	