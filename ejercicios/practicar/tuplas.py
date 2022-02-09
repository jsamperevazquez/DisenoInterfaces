tupla=("elemento1","elemento2","elemento3","elemento4",5) #es igual que la lista pero en vez de corchete lleva parentesis
milista=list(tupla) #creamos una lista a partir de una tupla
mitupla=tuple(milista) #creamos una tupla a partir de una lista
print(tupla[:])# Imprimimos toda la tupla

print(tupla[2])# Vemos que es una tupla porque te lo muestra entre parentesis

print(milista[:]) # Imprime entre corchetes

print(mitupla[:]) #Inmprime la tupla entre corchetes

print (5 in tupla)# imprime true o false dependiendo si está 5 o no en la tupla

print(tupla.count(5))# función count para que cuente el numero de veces que está 5 en la tupla.

print(len(tupla))# función len para que muestre el número de elementos de la tupla

tuplaunitaria=("angel",) # tupla con un solo elemento.Imprescindible la coma

print(tuplaunitaria)
print(len(tuplaunitaria))

otratupla="juan",12,"pepe" #Tupla sin parentesis (no aconsejable) se conoce como empaquetado de tupla
print(otratupla)

tupla_para_desempaquetar=("pato","perro",5,"loro",1.6)
animal1,animal2,numero1,animal3,numero2=tupla_para_desempaquetar# con esto estamos desempaquetando la tupla y asignando a cada variable el valor de cada elemento de la tupla.
print (animal2)
print (numero2)
print (animal1)
# Recordar que las tuplas no se pueden modificar (ejemplo append)



