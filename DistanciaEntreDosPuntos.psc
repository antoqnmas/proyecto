Algoritmo DistanciaEntreDosPuntos
	// Declaración de variables
    Definir X1, Y1, X2, Y2, Distancia Como Real
    
    // Entrada de datos
    Escribir "Ingrese la coordenada X1:"
    Leer X1
    Escribir "Ingrese la coordenada Y1:"
    Leer Y1
    Escribir "Ingrese la coordenada X2:"
    Leer X2
    Escribir "Ingrese la coordenada Y2:"
    Leer Y2
	
    // Cálculo de la distancia
    Distancia <- Raiz((X1 - X2)^2 + (Y1 - Y2)^2)
	
    // Mostrar el resultado
    Escribir "La distancia entre los puntos (", X1, ",", Y1, ") y (", X2, ",", Y2, ") es: ", Distancia

	
FinAlgoritmo
