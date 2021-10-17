print("programa de numeros mayores que el anterior")

numero=int(input("introduce un numero: \n"))
test=float("-inf")
if numero>test:
	test=numero
	numero=int(input("introduce un numero mayor al anterior: \n "))		
while numero>test:
	print("El numero introducido es mayor al anterior, sigue introduciendo numeros")
	test=numero
	numero=int(input("introduce otro numero mayor al anterior: \n "))
	if numero<test:
		print("incorrecto, el numeoro introducido es menor al anterior")
		break;





