# Archivo: CalculoDescuentoPython.py

# Función para calcular el descuento
def calcular_descuento(monto_compra, porcentaje_descuento=10):
    """
    Calcula el monto del descuento según el total de la compra.

    Parámetros:
        monto_compra (float): Total de la compra.
        porcentaje_descuento (float): Porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
        float: Monto del descuento calculado.
    """
    descuento = monto_compra * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Llamada 1: solo monto, se aplica el descuento por defecto (10%)
    monto1 = 150.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print(f"Compra 1: Monto = ${monto1:.2f}, Descuento = ${descuento1:.2f}, Total a pagar = ${total1:.2f}")

    # Llamada 2: monto + porcentaje de descuento personalizado
    monto2 = 200.0
    descuento2 = calcular_descuento(monto2, 20)  # Aquí uso 20%
    total2 = monto2 - descuento2
    print(f"Compra 2: Monto = ${monto2:.2f}, Descuento = ${descuento2:.2f}, Total a pagar = ${total2:.2f}")
