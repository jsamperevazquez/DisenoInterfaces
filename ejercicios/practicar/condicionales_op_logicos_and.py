print("operadores lógicos")
print("Derecho a becas")

#Las becas se darán a alumnos que vivan a más de 40kms,tres hijos y salario familiar <=20000

distancia_escuela=int(input("introduce la distancia a la escuela en kms: "))
print(distancia_escuela)

numero_hermanos=int(input("introduce numero de hermanos: "))
print(numero_hermanos)

salario_familiar=int(input("introduce el salario familiar en euros: "))
print(salario_familiar)

if distancia_escuela>= 40 and numero_hermanos >=3 and salario_familiar <20000: # Con el uso del operador and concateno condiciones y obligo a que se cumplan las tres, sino salta al else
	print("Tienen derecho a la beca")
else:
	print("sus condiciones no cumplen los requesitos para la beca")
