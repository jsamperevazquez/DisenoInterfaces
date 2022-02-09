diccionario = {"Espana": "Madrid", 23: "Jordan", "Alemania": "Berlin", 3.14: "numeroPI",
               "jugadores": 11}  # Diccionario mezclando diferentes tipos de elementos (string,enteros,floats)
print(diccionario)

mitupla = ["EEUU", "Italia", "Portugal"]  # Creo una tupla para asignar claves a cada uno de los valores
diccionario2 = {mitupla[0]: "Wasington", mitupla[1]: "Roma",
                mitupla[2]: "Lisboa"}  # asigno las claves de la tupla a cada valor del diccionario con el indice[]
print(diccionario2)

print(diccionario2["Italia"])  # Pido el valor de la clave Francia

diccionario3 = {23: "Jordan", "Nombre": "Michael", "Equipo": "Chicago", "anillos": [1991, 1992, 1993, 1996, 1997,
                                                                                    1998]}  # Almaceno dentro del diccionario una tupla llena de valores[]
print(diccionario3)

print(diccionario3["anillos"])  # Imprimo la tupla de valores de la clave anillos.

diccionario4 = {23: "Jordan", "Nombre": "Michael", "Equipo": "Chicago", "anillos": {
    "temporadas": [1991, 1992, 1993, 1996, 1997, 1998]}}  # Creo un diccionario dentro de otro diccionario (temporadas)

print(diccionario4["anillos"])  # Imprimo el diccionario que está dentro del diccionario principal

print(diccionario4)

print(diccionario4.keys())  # Imprime las claves del diccionario
print(diccionario4.values())  # Imprime los valores del diccionario
print(len(diccionario4))  # Imprime el número de elementos que tiene el diccionario

print(type(diccionario["Espana"]))  # Con esta función de pido que me diga de que clase es la clave Espana

print("Alemania" in diccionario)  # Con esto pregunto si está Alemania en diccionario

Diccionario_borrar_valores = {1: 2, 3: 4, 5: 6}
print(Diccionario_borrar_valores)
Diccionario_borrar_valores.clear()
print(Diccionario_borrar_valores)  # Con la función clear borro todo lo que está en el diccionario.
