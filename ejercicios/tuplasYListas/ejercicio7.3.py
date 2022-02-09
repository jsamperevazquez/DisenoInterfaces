tuplaNombres = ["Angel", "Pedro", "María", "Manuel", "Carlos"]
tuplaNomGene = (("Ángel", 'H'), ("Pedro", 'H'), ("María", 'M'), ("Manuel", 'H'), ("Carlos", 'H'))


def saludoCordial(lista):
    for n in lista:
        if (n[1]) == 'H':
            print("Estimado  %s" % n[:1])
        else:
            print("Estimada %s" % n[:1])


saludoCordial(tuplaNomGene)


def darPosicion(lista, posicion,numeroNombres):
    for n in range(posicion, posicion + numeroNombres):
        if lista[n][1] == 'H':
            print("Estimado %s" % lista[n][0])
        else:
            print("Estimada %s" % lista[n][0])


darPosicion(tuplaNomGene, 2, 2)
