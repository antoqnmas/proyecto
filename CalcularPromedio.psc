Algoritmo CalcularPromedio
	// Declarar variables
    Definir materia Como Texto
    Definir calificacion1, calificacion2, calificacion3, calificacion4, promedio Como Real
	
    // Solicitar el nombre de la materia
    Escribir "Introduce el nombre de la materia: "
    Leer materia
	
    // Solicitar las calificaciones
    Escribir "Introduce la calificación 1: "
    Leer calificacion1
	
    Escribir "Introduce la calificación 2: "
    Leer calificacion2
	
    Escribir "Introduce la calificación 3: "
    Leer calificacion3
	
    Escribir "Introduce la calificación 4: "
    Leer calificacion4
	
    // Calcular el promedio
    promedio <- (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4
	
    // Mostrar el promedio
    Escribir "El promedio de la materia ", materia, " es: ", promedio

FinAlgoritmo
