# Reto 39 - Planificador de Compra en Merca Nocturna
# Solución de referencia

def compra_maxima(presupuesto, productos):
    # productos=(nombre, precio_rebajado); maximiza cantidad con estrategia de menor precio
    compra = []
    restante = presupuesto
    for n, p in sorted(productos, key=lambda x: x[1]):
        if p <= restante:
            compra.append(n)
            restante -= p
    return compra, restante

print(compra_maxima(50000, [("arroz", 12000), ("leche", 5000), ("huevos", 14000), ("pan", 4000)]))
