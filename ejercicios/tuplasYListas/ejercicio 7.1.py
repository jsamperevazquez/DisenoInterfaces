miTupla = 3,4,5,2,1,8,9
def estaOrdenada(tupla):
    lista1 = tupla
    # El método sorted devuelve una lista ordenada y el método sort SIEMPRE DEVUELVE NONE
    lista2 = sorted(tupla)
    if lista1 != lista2:
        print("Lista desordenada")
    else:
        print("Lista ordenada")

estaOrdenada(miTupla)