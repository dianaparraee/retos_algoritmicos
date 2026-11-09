# Reto 23 - Calculadora de Costos Compartidos en Uber Pool
# Solución de referencia

def dividir_viaje(tarifa, distancias):
    total = sum(distancias)
    return {i + 1: round(tarifa * d / total, 2) for i, d in enumerate(distancias)}

print(dividir_viaje(30000, [5, 3, 2]))
