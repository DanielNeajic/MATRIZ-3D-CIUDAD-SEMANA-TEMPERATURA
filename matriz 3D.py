import random

# Definir el tamaño de la matriz 3D
num_ciudades = 3
dias_semana = 7
semanas = 4

# Crear una matriz 3D con temperaturas aleatorias
temperaturas = [[[random.randint(0, 20) for _ in range(dias_semana)] for _ in range(semanas)] for _ in range(num_ciudades)]

# Mostrar la matriz de temperaturas
print("Matriz de Temperaturas:")
for ciudad, ciudad_temperaturas in enumerate(temperaturas):
    print(f"Ciudad {ciudad + 1}:")
    for semana, semana_temperaturas in enumerate(ciudad_temperaturas):
        print(f"Semana {semana + 1}: {semana_temperaturas}")

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad, ciudad_temperaturas in enumerate(temperaturas):
    for semana, semana_temperaturas in enumerate(ciudad_temperaturas):
        promedio_semana = sum(semana_temperaturas) / len(semana_temperaturas)
        print(f"Promedio de temperaturas para Ciudad {ciudad + 1}, Semana {semana + 1}: {promedio_semana:.2f}°C")