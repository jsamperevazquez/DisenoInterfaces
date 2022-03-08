class Vehiculos():  # Creamos la superclase o clase padre
    def __init__(self, marca, modelo):  # Creamos el constructor para que todos los objetos tengan este estado inicial
        self.marca = marca  # self.marca= a la marca que le pasemos por parámetro.
        self.modelo = modelo  # self.modelo = al modelo que le pasemos por parámetro.
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):  # creamos un método para arroncar el vehículo

        self.enmarcha = True

    def acelerar(self):  # creamos un método para acelerar el vehículo

        self.acelera = True

    def frenar(self):  # creamos un método para frenar el vehículo

        self.frena = True

    def estado(self):  # creamos un método para que nos indique el estado del vehículo.
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ",
              self.acelera, "\nFrenando: ", self.frena)


class Furgoneta(Vehiculos):  # Creamos una clase que hereda estado de vehiculos
    def carga(self, cargar):  # Creamos un método propio para esta clase y le pasamos un parámetro
        self.cargado = cargar  # Recogemos el parámetro recibido y lo introducimos en el self.cargado
        if (self.cargado):  # si self.cargado es True
            return "La Furgoneta está cargada"
        else:
            return "La Furgoneta no está cargada"


class Moto(Vehiculos):  # Creamos una clase moto y dentro de los paréntesis va la clase de la que queremos heredar
    hcaballito = ""

    def caballito(
            self):  # Creamos un método para la clase moto;tiene un comportamiento más que un vehículo no tiene; tiene los métodos heredados mas el suyo propio.
        self.hcaballito = "Voy haciendo un caballito"

    # A continuación vamos a hacer lo que se conoce como sobreescritura de métodos:
    def estado(
            self):  # copiamos el estado del metodo de la clase padre(con esto sobreescribimos el estado inicial y ya tiene su propio estado) y añadimos la propiedad o comportamiento propio de esta clase.
        print("Marca: ", self.modelo, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ",
              self.acelera, "\nFrenando: ", self.frena, "\n",
              self.hcaballito)  # Cuando una clase hereda de otra como esta, al llamar al método estado de la clase moto, se muestra esta porque la heredada es sobreescrita por la propia.


class VElectricos():

    def __init__(self):
        self.autonomía = 100

    def cargarEneria(self):
        self.cargando = True


miMoto = Moto("Honda", "CBR")  # Tenemos que pasarle marca y modelo porque también heredamos del constructor.

miMoto.arrancar()

miMoto.caballito()  # LLamamos al metodo de caballito y entra el método con lo cual hcaballito (cadena de caracteres
# vacías) toma el valor de dentro del método(self.hcaballito).

miMoto.estado()

miFurgo = Furgoneta("Renault", "Kangoo")

miFurgo.arrancar()

miFurgo.estado()

print(miFurgo.carga(True))  # Tenemos que poner el print porque el return es una cadena de caracteres.


# HERENCIA MÚLTIPLE# A continuación vamos a heredar de dos clases(se puede heredar de varias clases). *****Siempre
# Siempre**** hereda del constructor de la primera clase que nombres en el paréntesis
class BicicletaElectrica(Vehiculos, VElectricos):  # esta clase hereda de vehiculos y Velectricos
    # Class BicicletaElectrica(VElectricos,Vehiculos): #Si desbloqueas esta linea y comentamos la anterior heredará
    # del constructor VElectricos y va a dar error porque VElectricos no solicita parámetro
    pass


mibici = BicicletaElectrica("Orbea", "HDR100")
mibici.estado()
