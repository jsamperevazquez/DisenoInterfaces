# yield from simplifica el código de los generadores en el caso de utilizar bucles anidados.
def devuleve_ciudades(*ciudades): # el * significa que va a recibir un numero indeterminado de elementos, en forma de tupla.
	for elemento in ciudades:
		yield elemento # El elemento es Madrid,Barcelona,etc...

ciudades_devueltas=devuleve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))


def devuleve_ciudades(*ciudades): # el * significa que va a recibir un numero indeterminado de elementos, en forma de tupla.
	for elemento in ciudades:
		for subelemento in elemento:
			yield subelemento # El subelemento es M,a,d, etc...(las letras que forman las palabras)

ciudades_devueltas=devuleve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

# Con yield from 

def devuleve_ciudades(*ciudades): # el * significa que va a recibir un numero indeterminado de elementos, en forma de tupla.
	for elemento in ciudades:
		yield  from elemento # yield from nos permite prescindir del for anidado. Hace un yield desde el primer elemento.

ciudades_devueltas=devuleve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
