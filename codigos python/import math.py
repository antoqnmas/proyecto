import math

# Pedir al usuario que ingrese las coordenadas de los 2 puntos
x1 = float(input("Ingrese la coordenada x del punto 1: "))
y1 = float(input("Ingrese la coordenada y del punto 1: "))
x2 = float(input("Ingrese la coordenada x del punto 2: "))
y2 = float(input("Ingrese la coordenada y del punto 2: "))

# Calcular la distancia entre los 2 puntos
distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Mostrar la distancia
print(f"La distancia entre los 2 puntos es: {distancia:.2f}")
