# Programa para calcular el promedio de un estudiante

print("=== SISTEMA DE PROMEDIO ===")

# Pedir nombre del estudiante
nombre = input("Ingresa el nombre del estudiante: ")

# Pedir cantidad de materias
cantidad = int(input("¿Cuántas materias tiene el estudiante?: "))

suma = 0

# Ciclo para ingresar calificaciones
for i in range(cantidad):
    while True:
        calificacion = float(input(f"Ingrese la calificación {i+1} (0-10): "))
        
        if 0 <= calificacion <= 10:
            suma += calificacion
            break
        else:
            print("Error: La calificación debe estar entre 0 y 10.")

# Calcular promedio
promedio = suma / cantidad

# Mostrar resultados
print("\n=== RESULTADOS ===")
print("Estudiante:", nombre)
print("Promedio final:", round(promedio, 2))

# Evaluar si está aprobado
if promedio >= 6:
    print("Estado: APROBADO")
else:
    print("Estado: REPROBADO")