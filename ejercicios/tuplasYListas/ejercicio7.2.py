# Declaraciones
ficha1 = (3, 4)
ficha2 = (5, 4)
cadena1 = "3-4"
cadena2 = "3-5"


def fichas(f1, f2):
    for i in ficha1:
        for j in ficha2:
            if i == j:
                print(f"El número {i} de la {ficha1} encaja con el número {j} de la ficha {ficha2}")
            else:
                print(f"Los números {i, j} no encajan")


fichas(ficha1, ficha2)


def fichascadena(c1, c2):
    lista1 = c1.split('-')
    lista2 = c2.split('-')
    for i in lista1:
        for j in lista2:
            if i == j:
                print(f"El número {i} de la {lista1} encaja con el número {j} de la ficha {lista2}")
            else:
                print(f"Los números {i, j} no encajan")


fichascadena(cadena1, cadena2)
