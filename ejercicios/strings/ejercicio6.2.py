def separar(cadena, caracter):
    palabra = ""
    contador = 0
    for i in cadena:
        if len(cadena) - 1 == contador:
            palabra += i
            break
        else:
            palabra += i + caracter
        contador += 1
    return palabra


print(separar("hola", ","))
