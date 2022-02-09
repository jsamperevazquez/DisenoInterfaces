def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	try: # con try le decimos que intente hacer la operacion, y si no puede que vaya al except
		return num1/num2
	
	except ZeroDivisionError: # si no pudo hacer la operacion de la division por 0, le damos el nombre del error,tiene que coincidir con el error (muy importante para que el programa continue), para que siga con el codigo y no caiga.
		print("No se puede dividir entre 0")
		return "Operacion erronea"

while True: # bucle infinito mientras sea cierto 
	try:
		op1=int(input("introduce el primer numero: "))

		op2=int(input("introduce el segundo numero: "))
		break;	# si introducimos un parametro erroneo en los input no lee el brake sino que salta al except
	except ValueError:
		print("los datos introducidos no son correctos, intentalo de nuevo")
operacion=input("introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))
# Si se divide por 0 el programa cae (ZERODIVISIONERROR) y el resto de codigo no se ejecutaria
# La solucion de esto es una captura o control de excepcion para intentar realizar la instruccion e en el caso
# de no poder sigue con el codigo.

else:
	print("Operacion no valida")

# Con la excepcion creada seguira el programa
print("Operacion ejecutada. Continuacion de ejecucion del programa ")