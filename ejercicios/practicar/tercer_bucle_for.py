for i in range(5):
	print(f"valor de la variable {i}") # con la función f le decimos al programa que queremos hacer una anotación especial de concatenado (Concatenamos el texto con el valor de la variable i).

for j in range(5,10): # Va desde el 5 hasta el 9
	print(f"valor de la variable{j}")

for v in range(5,50,3): # Tiene que empezar en el 5, ir hasta el 49, e ir de 3 en 3.
	print (f"valor de la variable{v}")

print(len("Angel")) #Nos devuelve la longitud de caracteres del string.

valido=False
email=input("introduce email: \n")
for i in range(len(email)): # Le damos el rango del for de la longitud del email.
	if email[i]=="@":
		valido=True
if valido:
	print("email correcto")
else:
	print("email incorrecto")
	