# Reto 25 - Control de Préstamos y Penalizaciones de Biblioteca
# Solución de referencia

def multa_biblioteca(hora_prestamo, hora_devolucion, tarifa_min=100):
    retraso = max(0, hora_devolucion - hora_prestamo - 120)
    return retraso, retraso * tarifa_min

print(multa_biblioteca(18 * 60, 20 * 60 + 15))
