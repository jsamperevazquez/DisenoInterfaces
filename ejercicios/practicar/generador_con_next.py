def numerosPares(limite):  # vamos a poner un (limite) para que no me genere numeros pares infinitos.

    num = 1  # inicio la varible en 1 (primer numero impar)

    while num < limite:
        yield num * 2

        num = num + 1


devuelvepares = numerosPares(20)  # en la variable almacenamos el resultado del objeto iterable
# print(numerosPares(20)) ya no se necesita.

print(next(devuelvepares))  # Imprime el primer valor que tiene el objeto itinerable

print("Aqui podria ir mas codigo...")

print(next(devuelvepares))  # Imprime el segundo valor que tiene el objeto itinerable

print("Aqui podria ir mas codigo...")

print(next(devuelvepares))  # Imprime el tercer valor que tiene el objeto itinerable

print("Aqui podria ir mas codigo...")
