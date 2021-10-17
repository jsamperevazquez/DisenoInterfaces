""" Conceptos de la POO
Vocabulario de la POO:
* Clase: Modelo donde se redactan las características comunes de un grupo de objetos.
* Ejemplar de clase (instancia y objeto de clase son sinónimos): ejemplar (objeto o intancia) perteneciente a una clase.
* Modularización: Una aplicación puede estar compuesta de varias clases. La modularización permite reutilizar código de un programa en otro.
* Encapsulación: El funcionamiento interno de una clase concreta no sabe del funcionamiento de las otras clases, pero de alguna forma están conectadas entre sí mediante métodos de acceso.

Para poder acceder a las propiedades y comportamiento de los objetos se usa la nomenclatura del punto.
Ejemplo:
Haciendo analogía de coche como objeto
"""
class Coche(): # La primera latra de la clase siempre en mayúscula
	# Estas son las propiedades de la clase, todos los objetos que pertenezcan a esta clase tendrán estas propiedades
	largoChasis=250 
	anchoChasis=120
	ruedas=4
	enmarcha=False

	# Ahora los comportamientos de los objetos
	# Para ello se crea un método (defs), el método es una función que pertenece a una clase.
	def arrancarCoche(self): # Self hace referencia al propio objeto que pertenece a la clase.
		self.enmarcha=True

	def estado(self): #Creamos un método para comprobar el estado del coche
		if(self.enmarcha): # Esto es lo mismo que self.enmarcha==True
			
			return "El coche está en marcha"

		else:
			
			return "El coche está parado"

# Creamos nuestros objetos de la clase:

miCoche=Coche() # Esto es instanciar una clase o ejemplarizar una clase (crear objeto)

# Para acceder a las propiedades del objeto se usa la nomenclatura del punto:
print("El largo del coche es: " ,miCoche.largoChasis)
print("El coche tiene ",miCoche.ruedas," ruedas")

miCoche.arrancarCoche() # Hacemos una llamada al metodo, ese método recibe por parámetro es el propio objeto, miCoche se almacena en el self de el método.(arranca el coche)

print(miCoche.estado()) 