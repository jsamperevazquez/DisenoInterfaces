cadena = "Practicando python"


def dos_primeros(string):
    contador = 0
    caracteres = ""

    for i in string:
        caracteres += i
        contador += 1
        if contador == 2:
            return caracteres


def tres_ultimos(string):
    contador = 0
    caracteres = ""
    for i in string:
        contador += 1
        if contador == len(string) - 2 or contador == len(string) - 1 or contador == len(string):
            caracteres += i
    return caracteres


def cada_tres(string):
    caracteres = string[::2]
    return caracteres


def al_reves(string):
    caracteres = string[::-1]
    return caracteres


def al_derecho_reves(string):
    caracteres = cadena + chr(27) + "[1;33m" + " al revés: " + chr(27) + "[1;37m" + cadena[::-1]
    return caracteres


print(dos_primeros(cadena))
print(tres_ultimos(cadena))
print(cada_tres(cadena))
print(al_reves(cadena))
print(al_derecho_reves(cadena))
