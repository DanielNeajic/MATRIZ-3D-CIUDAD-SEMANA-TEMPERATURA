def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_a_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def convertir_a_fahrenheit_y_kelvin(celsius):
    fahrenheit = celsius_a_fahrenheit(celsius)
    kelvin = celsius_a_kelvin(celsius)
    return fahrenheit, kelvin

# Ejemplo de uso:
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit, kelvin = convertir_a_fahrenheit_y_kelvin(celsius)
print("{:.2f} grados Celsius equivalen a {:.2f} grados Fahrenheit y {:.2f} grados Kelvin.".format(celsius, fahrenheit, kelvin))
