# Reto 16 - Disponibilidad de Salas de Cómputo e Impresiones
# Solución de referencia

def tiempo_impresion(paginas, impresoras, personas_fila, min_por_pagina=0.5):
    if impresoras <= 0:
        return float("inf")
    espera = personas_fila * 2
    impresion = paginas * min_por_pagina / impresoras
    return espera + impresion

print(tiempo_impresion(40, 2, 5))
