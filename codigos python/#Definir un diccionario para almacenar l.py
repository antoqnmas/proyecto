#Definir un diccionario para almacenar las calificaciones
calificaciones = {}

#Pedir al usuario que ingrese el número de materias
num_materias = int(input("Ingrese el número de materias: "))

#Pedir al usuario que ingrese las calificaciones para cada materia
for i in range(num_materias):
    materia = input(f"Ingrese el nombre de la materia {i+1}: ")
    calificacion = float(input(f"Ingrese la calificación de {materia}: "))
    calificaciones[materia] = calificacion

#Calcular el promedio de calificaciones
promedio = sum(calificaciones.values()) / num_materias

#Mostrar el promedio de calificaciones
print(f"El promedio de calificaciones es: {promedio:.2f}")

#Mostrar las calificaciones para cada materia
print("Calificaciones por materia:")
for materia, calificacion in calificaciones.items():
    print(f"{materia}: {calificacion:.2f}")
