# Reto 29 - Monitor de Deuda de Sueño Semanal
# Solución de referencia

def deuda_sueno(horas):
    racha = 0
    mayor = 0
    for h in horas:
        racha = racha + 1 if h < 5 else 0
        mayor = max(mayor, racha)
    deuda = sum(max(0, 7 - h) for h in horas)
    return deuda, mayor >= 2

print(deuda_sueno([6, 4, 4, 7, 6, 5, 7]))
