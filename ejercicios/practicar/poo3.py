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


class Coche():  # La primera latra de la clase siempre en mayúscula
    # Estas son las propiedades de la clase, todos los objetos que pertenezcan a esta clase tendrán estas propiedades

    def __init__(
            self):  # Esta función es un constructor para dar a nuestra clase un estado inicial claro (el objeto va a tener ese estado inicial)
        self.__largoChasis = 250  # Dentro de un constructor las propiedades tienen que ir precedidas de un self.
        self.__anchoChasis = 120  # Las variables que deseamos que no se puedan cambiar de estado inicail deben empezar por __
        self.__ruedas = 4  # con los __ se encapsula esta variable para que no se puedan cambiar desde fuera de la clase
        self.__enmarcha = False

    # A partir de ahora se debe llamar a cada variable de la clase por su nombre real (ejemplo: __largoChasis) con los __ incluidos.

    # Ahora los comportamientos de los objetos
    # Para ello se crea un método (defs), el método es una función que pertenece a una clase.
    def arrancarCoche(self,
                      arrancamos):  # Self hace referencia al propio objeto que pertenece a la clase y solicitamos un parámetro que sea True or False
        self.__enmarcha = arrancamos  # self.__enmarcha parte en False y metemos el resultado del parámetro que pedimos (true or false) dentro de la variable enmarcha
        if self.__enmarcha:  # si __enmarcha es =True
            chequeo = self.__chequeo_interno()  # Hacemos el chequeo cuando el coche está arrancado;El resultado del método encapsulado chequeo (True or False) se guarda en chequeo

        if (self.__enmarcha and chequeo):  # Si enmarcha es = True y el chequeo es todo ok.
            return "El coche está arrancado"
        elif (self.__enmarcha and chequeo == False):  # Si está arrancado y el chequeo es False
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche está parado"

    def estado(self):  # Con este método vamos a imprimir las propiedades de nuestra clase.
        print("El coche tiene: ", self.__ruedas, "ruedas. Un ancho de: ", self.__anchoChasis, "y un largo de: ",
              self.__largoChasis)

    def __chequeo_interno(
            self):  # Creamos un método para chequear nuestro coche,con los __ lo que hacemos es encapsular el método para que no se pueda acceder fuera de la clase.
        print("realizando chequeo interno")
        self.gasolina = "ok"  # Creamos nuestras variables dentro del módulo
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False


# Creamos nuestros objetos de la clase:

miCoche = Coche()  # Esto es instanciar una clase o ejemplarizar una clase (crear objeto)

# Para acceder a las propiedades del objeto se usa la nomenclatura del punto:
print(miCoche.arrancarCoche(
    True))  # Hacemos una llamada al metodo, ese método recibe por parámetro es el propio objeto (self), miCoche se almacena en el self de el método.Tiene que ir con print porque el return de la función devuelve string(arranca el coche porque le pasamos True)

miCoche.estado()  # Devuelve las propiedades de la clase (va sin print porque el módulo ya lleva print)
# print (miCoche.__chequeo_interno()) # Si desbloqueamos esta linea hacemos una llamada al método de chequeo va a dar error porque está encapsulado y se hace la llamada desde fuera de la clase.
print("A continuación creamos el segundo objeto--------------------------------------------------------")

miCoche2 = Coche()  # comparten las mismas propiedades

# miCoche2.__ruedas=2 # Intetamos cambiar el valor de nuestro estado inicial desde fuera de la clase (No va a ser posible porque está encapsulado con __) 
print(miCoche2.arrancarCoche(False))  # En esta ocasión le pasamos False(el coche está parado)
miCoche2.estado()
