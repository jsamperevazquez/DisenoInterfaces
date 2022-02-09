email=input("introduce tu email por favor:\n")

for i in email:

	if i =="@": # En cuanto la i valga @ el bucle for romperá con lo cual ya no pasará por else ya que pertenece al for.
		arroba=True

		break;

else: #Este else no forma parte del if sino del for. El else dentro de un bucle no forma parte de un condicional, se ejecuta cuando el bucle ha terminado.Una vez terminado el flujo del bucle pasa al else
	arroba=False

print(arroba)