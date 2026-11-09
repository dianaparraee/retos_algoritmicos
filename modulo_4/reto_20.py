# Reto 20 - Monitor de Clima y Paso por Encharcamientos
# Solución de referencia

def clima(rain, avenidas):
    inundadas = [nombre for nombre, nivel in avenidas if nivel >= 7]
    if rain >= 7 or len(inundadas) >= 2:
        return "Retrasar salida o usar ruta alternativa", inundadas
    return "Salida normal con precaución", inundadas

print(clima(8, [("AutoNorte", 8), ("Calle80", 6), ("Calle13", 3)]))
