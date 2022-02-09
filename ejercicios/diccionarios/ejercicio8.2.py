import random


def veces_Aparece_palabra(frase):
    diccionario = dict()  # Constructor de diccionario
    palabra = frase.split()
    for i in palabra:
        if i.lower() in diccionario:
            diccionario[i.lower()] = diccionario[i.lower()] + 1
        else:
            diccionario[i.lower()] = 1
    return diccionario


def veces_Aparece_caracter(frase):
    diccionario = dict()
    for i in frase.replace(" ", ""):
        if i in diccionario:
            diccionario[i.lower()] = diccionario[i.lower()] + 1
        else:
            diccionario[i.lower()] = 1

    return diccionario


def tirar_dados(tiradas):
    diccionario = dict()
    for i in range(0, tiradas):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        diccionario["Dado1"] = dado1
        diccionario["Dado2"] = dado2
        diccionario["Suma"] = dado1 + dado2
        print(f"La suma de {diccionario['Dado1']} + {diccionario['Dado2']} es {diccionario['Suma']} ")


print(veces_Aparece_palabra("En un lugar un de la mancha"))

print(veces_Aparece_caracter("Hola don pepito"))

tirar_dados(3)
