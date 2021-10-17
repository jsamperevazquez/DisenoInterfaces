# Generadores son estructuras que extraen valores de una función y se almacenan en objetos iterables(que se pueden recorrer)
# Los valores se almacenan de uno en uno
# Cada vez que un generador almacena un valor, este permanece en un estado pausado hasta que se solicita el siguiente. Esta característica es conocida como "suspensión de estado"

# Ventajas
# Son más eficientes que las funciones tradicionales
# muy útiles con listas de valores infinitos 
# Bajo determinados escenarios, será muy útil que un generador devuelva los valores de uno en uno.

print("vamos a comparar una función con un generador")

#Funcion: 

def numerosPares(limite): # vamos a poner un (limite) para que no me genere numeros pares infinitos.
	
	num=1 #inicio la varible en 1 (primer numero impar)

	milistapares=[] # Creo una lista vacia

	while num<limite: 
		
		milistapares.append(num*2) #Meto el 2 en mi lista como el primer par

		num=num+1 

	return milistapares
	
	
print(numerosPares(20))

#Generador:
def numerosPares(limite): # vamos a poner un (limite) para que no me genere numeros pares infinitos.
	
	num=1 #inicio la varible en 1 (primer numero impar)

	# milistapares=[] # Esto ya no se necesita porque crea un objeto iterable

	while num<limite: 
		
		
		# milistapares.append(num*2) #Ya no se necesita esta linea porque la lista la va generando.

		yield num*2 # Devueve los elementos varias veces a traves de un generador. 

		num=num+1 

	# return milistapares   Esta no se necesita porque tenemos el yield
	
devuelvepares=numerosPares(20) # en la variable almacenamos el resultado del objeto iterable
# print(numerosPares(20)) ya no se necesita.


for i in devuelvepares: #recorro con un bucle el objeto iterable
	print(i)








