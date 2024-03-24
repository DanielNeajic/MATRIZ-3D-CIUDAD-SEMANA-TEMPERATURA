def calcular_temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de cada ciudad en un período de tiempo.

    Args:
        datos (dict): Un diccionario donde las claves son nombres de ciudades y los valores son listas de temperaturas.

    Returns:
        dict: Un diccionario donde las claves son nombres de ciudades y los valores son las temperaturas promedio.
    """
    promedios = {}
    for ciudad, temperaturas in datos.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio
    return promedios

# Ejemplo de datos: temperaturas de 3 ciudades durante 4 semanas
datos = {
    'Puyo A': [20, 22, 24, 19],
    'Ambato B': [18, 17, 16, 15],
    'Riobamba C': [23, 25, 22, 20]
}

# Llamada a la función para calcular el promedio de temperaturas
promedios_ciudades = calcular_temperatura_promedio(datos)

# Obtener el promedio para la ciudad de Puyo
promedio_puyo = promedios_ciudades['Puyo A']

# Imprimir el resultado
print("El promedio de temperatura para la ciudad de Puyo es:", promedio_puyo)
