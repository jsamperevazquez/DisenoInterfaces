for letra in "Python":
	
	if letra=="h":
		continue # lo que hace el programa es que cuando letra valga h ignorará el resto del bucle (ignora la frase del print), pasa a la siguiente vuelta de bucle.

	print("viendo la letra: " + letra)



nombre="pildoras informaticas"

print(len(nombre)) #imprime todos los caracteres(incuyendo los espacios en blanco).No cuenta letras solo.

contador=0
for i in nombre:
	if i==" ": #Con esto decimos que cuando i valga un espacio en blanco, salte el bucle y vuelva al principio de este.
		continue
	contador=contador +1

print(contador)