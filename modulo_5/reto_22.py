# Reto 22 - Gestión de Inventario en Minimarkets Cercanos
# Solución de referencia

def inventario(productos):
    criticos = [(n, s) for n, s in productos.items() if s < 5]
    mas_vendido = max(productos, key=productos.get)
    return criticos, mas_vendido

print(inventario({"Arroz": 3, "Agua": 12, "Galletas": 4}))
