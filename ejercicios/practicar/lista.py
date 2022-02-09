mi_lista=["angel","pablo","guille","Ramón"]

print (mi_lista[:]) #Imprime toda la lista(array)

print (mi_lista[2]) #Imprime el tercer elemento ya que se empieza siempre en posición 0

print (mi_lista[-1]) #El negativo empieza a contar por el final (empieza en el 1, no en 0)

mi_lista.append("Juan") #función para agregar elemento al final de la lista

print (mi_lista[0:2]) # Esto es una porción de la lista (del 0 al 2.El 0 incluido el 2 no)

print (mi_lista[:2]) #forma abreviada igual a la anterior. Sobreentiende que empieza en 0

mi_lista.insert(3,"Patri") # Función para agregar elemento en posición deseada

print (mi_lista[1:2])# incluye el primero pero no el segundo

mi_lista.extend(["Santi","Leo"])# Función para agregar varios elementos al final de la lista

print(mi_lista[2:])# desde el indice 2 hasta el final de la lista

print (mi_lista.index("Patri")) #Funcion para devolver el indice en el que está patri

print ("pepe" in mi_lista)

print ("angel" in mi_lista)# Con esto comprueba si está el elemento en la lista

mi_lista.insert(2,9)# Con esto inserto en la posición 3 (empieza en 0) el elemento 9

print(mi_lista[:])

print(9 in mi_lista)

mi_lista.remove("Patri") #Con esto elimino a patri de mi lista

print(mi_lista[:])

mi_lista.pop() # Con esta función se elimina el ultimo elemento de la lista.

print (mi_lista[:])

milista2=["Sandra","Lucia"]

milista3=mi_lista+milista2 #Suma las listas (Concatena)

print (milista3[:])

mi_lista=mi_lista * 3 #Repite esta lista tres veces

print(mi_lista[:])