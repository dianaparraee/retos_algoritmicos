# Reto 13 - Ruta Segura y Mapeo de Zonas Iluminadas
# Solución de referencia

def ruta_segura(rutas):
    # ruta = (nombre, iluminación_0a10, comercio_0a10, policía_0a10)
    return max(rutas, key=lambda r: .5 * r[1] + .3 * r[2] + .2 * r[3])

print(ruta_segura([("A", 8, 5, 7), ("B", 6, 9, 8), ("C", 9, 4, 6)]))
