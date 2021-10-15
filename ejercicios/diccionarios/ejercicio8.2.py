def veces_Aparece_palabra(frase):
    diccionario = dict()  # Constructor de diccionario
    palabra = frase.split()
    for i in palabra:
        if i.lower() in diccionario:
            diccionario[i.lower().lower()] = diccionario[i.lower()] + 1
        else:
            diccionario[i.lower()] = 1
    return diccionario


print(veces_Aparece_palabra("En un lugar un de la mancha"))
