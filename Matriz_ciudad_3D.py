def calcular_temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de cada ciudad en un período de tiempo.

    Args:
        datos (dict): Un diccionario donde las claves son nombres de ciudades y los valores son listas de temperaturas.

    Returns:
        dict: Un diccionario donde las claves son nombres de ciudades y los valores son las temperaturas promedio.
    """
    promedios = {}
    for CIUDAD, temperaturas in datos.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[CIUDAD] = promedio
    return promedios

# Ejemplo de datos: temperaturas de 3 ciudades durante 4 semanas
datos = {
    'Puyo A': [20, 22, 24, 19],
    'Ambato B': [18, 17, 16, 15],
    'Riobamba C': [23, 25, 22, 20]
}

# Llamada a la función para calcular el promedio de temperaturas
promedios_ciudades = calcular_temperatura_promedio(datos)

# Imprimir los resultados
for ciudad, promedio in promedios_ciudades.items():
    print(f"La temperatura promedio en {ciudad} es: {promedio}")