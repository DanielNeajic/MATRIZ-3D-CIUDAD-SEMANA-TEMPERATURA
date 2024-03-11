def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Args:
    monto_total (float): Monto total de la compra.
    porcentaje_descuento (float, optional): Porcentaje de descuento a aplicar. Por defecto es 10.

    Returns:
    float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función desde el programa principal
monto_compra1 = 100


monto_compra2 = 100
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

# Muestra los resultados
print("Llamada 1:")
print(f"Monto total de la compra: ${monto_compra1}")

print("Llamada 2:")
print(f"Monto total de la compra: ${monto_compra2}")
print(f"Porcentaje de descuento: {porcentaje_descuento2}%")
print(f"Monto del descuento: ${descuento2}")
print(f"Monto final a pagar después del descuento: ${monto_final2}")
