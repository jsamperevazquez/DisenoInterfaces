"""La herencia se trata de trasladar el comportamiento de la herencia de la vida real a código"""
"""La herencia va también en jerarquías.La clase superior es la superclase.
La principal utilidad de las herecias en la programación es la reutilización de código. Cuando se crean objetos similares se heredan partes del código."""

class vehiculos(): # Creamos la superclase o clase padre
	def __init__(self, marca, modelo): #Creamos el constructor para que todos los objetos tengan este estado inicial
		self.marca=marca # self.marca= a la marca que le pasemos por parámetro.
		self.modelo=modelo # self.modelo = al modelo que le pasemos por parámetro.
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self): #creamos un método para arroncar el vehículo
		
		self.enmarcha=True

	def acelerar(self): #creamos un método para acelerar el vehículo
		
		self.acelera=True

	def frenar(self): #creamos un método para frenar el vehículo
		
		self.frena=True

	def estado(self): # creamos un método para que nos indique el estado del vehículo.
		print("Marca: ", self.modelo, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)



class Moto(vehiculos): # Creamos una clase moto y dentro de los paréntesis va la clase de la que queremos heredar
	pass #para que no de error al dejarla vacía

miMoto=Moto("Honda","CBR") #Tenemos que pasarle marca y modelo porque también heredamos del constructor.
miMoto.arrancar()
miMoto.estado()
