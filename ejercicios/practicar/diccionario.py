mi_diccionario={"Espana":"Madrid","Francia":"Paris","Alemania":"Berlin"} #Diccionario paises con sus capitales se pone clave:valor
mi_diccionario["Italia"]="Lisboa"#agrego un elemeto a mi diccionario mal adrede para modificarlo desués
print(mi_diccionario)
mi_diccionario["Italia"]="Roma"#Modifico el valor de la clave Italia, lo sobreescribe, nunca se pueden tener dos claves iguales
print(mi_diccionario)
del mi_diccionario["Alemania"] #Borro el elemento Alemania del diccionario
print(mi_diccionario)






print(mi_diccionario["Francia"])#le doy la clave para que me de el valor
