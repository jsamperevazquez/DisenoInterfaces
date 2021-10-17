print("Programa de suma de positivos")
numero=int(input("Introduce un numero positivo:\n"))
if numero<0:
	print("El numeoro introducido debe ser positivo")
else:
	lista=[numero]
while numero>0:
	print("El numero introducido es correcto")
	numero=int(input("Introduce un numero positivo: \n"))
	if numero>0:
		lista.append(numero)
		suma=0
		for i in lista:
			suma=suma+i
	else:
			print("El número introducido es incorrecto")
			break;
print("la suma de los positivos es " + str(suma))
print("fin de programa")
