# Reto 08 - Comparador de Combo Comida Rápida Nocturna
# Solución de referencia

def mejor_combo(opciones):
    # opción = (nombre, precio, nutricion_0_a_10, minutos)
    viables = [(n, p, nut, t) for n, p, nut, t in opciones]
    return min(viables, key=lambda x: x[1] + 500 * x[3] - 1000 * x[2])

print(mejor_combo([("A", 18000, 6, 10), ("B", 15000, 7, 20), ("C", 22000, 9, 5)]))
