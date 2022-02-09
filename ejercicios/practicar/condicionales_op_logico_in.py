print("Elección de asignaturas optativas")
print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

asignatura = input("Escribe la asignatura escogida:\n")
conversion = asignatura.capitalize()  # función capitalize() convierte la primera letra de la frase a mayúscula
if conversion in ("Informatica grafica", "Pruebas de software", "Usabilidad y accesibilidad"):
    print("Has elegido " + conversion + " como optativa ")

else:
    print(conversion + " es una asignatura no válida")
