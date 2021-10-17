for i in ["pildoras","informáticas",3]:
	print("Hola", end="  ")# el argumento end determina como queremos que termine la impresión (es como decirle que no haga salto de linea)

for j in "elotrolado": # realiza los argumentos del for tantas veces como caracteres tiene la palabra después del in
	print ("hola")	

email=False #variable boleana (En python True y False tienen la primera letra mayúscula)

for v in "angelsamperegmail.com":# la variable v va cogiendo el valor de cada string en cada vuelta, llega un momento que v=@ 
	if (v=="@"): #Cuando valga @ cambiamos el valor a true
		email=True
if email: #Esto es lo mismo que if email==true, si es true imprimirá correcto (solo comprobamos si lleva @ el correo)
	print("email correcto")
else:
	print("El email es incorrecto")


comprobacion1=False
comprobacion2=False
miemail=input("Introduce tu dirección de correo: \n")
contador=0 #Pongo un contador antes de entrar en el for.
for z in miemail:
	if (z=="@"):
		lista=(z) #Cada vez que entra en el if porque la variable z=@ lo mete en una lista.
		comprobacion1=True #Cambio el valor de la primera comprobación a true
		contador=contador+1 # sumo 1 al contador (si un correo tiene más de una @ es correo falso)
	if (z=="."):
		lista=(z) #Cada vez que la variable z adquiera el valor de . lo meto en la lista anterior
		comprobacion2=True	# Cambio el valor de la segunda comprobación a true.
if comprobacion1==True and comprobacion2==True and contador<=1 and lista[-1]!="@": #Hago un condicional para comprobar que se cumplan las dos comprobaciones, que el contador del @ no sea superior a 1 y que el último elemento de la lista de "@" y "." no sea un @.
	print("Email correcto")
else:
	print ("Email incorrecto")

for f in range(5):
	print(f)


