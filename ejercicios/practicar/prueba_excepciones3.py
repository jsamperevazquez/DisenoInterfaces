def divide ():
	
	try:
		op1=float(input("introduce el primer número"))
	
		op2=float(input("introduce el segundo número"))
	
		print("La división es :" + str(op1/op2))
	
	# Vamos a simplificar el código introduciendo varios except seguidos

	except ValueError:
		
		print("el valor introdicido es erroneo")
	
	except ZeroDivisionError:
		
		print ("No se puede dividir entre cero")
	
	finally: # Lo que venga a continuación se ejecutará siempre, tanto si entra en excepts como si no.
	
		print("Cálculo finalizado")

divide()