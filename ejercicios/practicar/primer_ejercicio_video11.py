print("Ejercicio 1 video 11")

numero1=int(input("Dame el primer numero\n"))
numero2=int(input("Dame el segundo numero\n"))

def DevuelveMax():
	if numero1>numero2:
		return(numero1)
	elif numero1==numero2:
		print ("Los numeros son iguales")
	else:
		return(numero2)

print(DevuelveMax())