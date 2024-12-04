#Pedir al usuario que ingrese el número de días
dias = int(input("Ingrese el número de días: "))

#Calcular el número de segundos
segundos_por_dia = 24 * 60 * 60
total_segundos = dias * segundos_por_dia

#Mostrar el resultado
print(f"El número de segundos en {dias} días es: {total_segundos}")
