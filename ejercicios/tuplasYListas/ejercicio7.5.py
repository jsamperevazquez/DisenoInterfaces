listaNumeros = (1, 4, 7, 2, 5, 11)


def devolverPrimos(listaN):
    primos = []
    for i in listaN:
        con = 0
        if i == 2:
            primos.append(i)
        else:
            for j in range(1, i + 1): # Recordamos que en range() el final del rango es excluyente (n, n-1)
                if i % j == 0:
                    con += 1
            if con == 2:
                primos.append(i)
    return primos


def sumatoria_Promedio(lista):
    sumatorio = 0
    contador = 0

    for i in lista:
        sumatorio += i
        contador += 1

    print("El sumatorio de la lista dadas es de %s" % sumatorio)
    print("El promedio de la lista dada es: %s" % (sumatorio / contador).__round__(2))  # round para mostrar 2 decimales


def factorial(lista):
    for i in lista:
        cont = 1
        factor = 1
        while cont <= i:
            factor = cont * factor
            cont += 1
        print(f"{i}!= {factor}")


print(devolverPrimos(listaNumeros))
sumatoria_Promedio(listaNumeros)
factorial(listaNumeros)
