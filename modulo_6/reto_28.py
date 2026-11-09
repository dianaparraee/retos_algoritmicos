# Reto 28 - Evaluador del Impacto de Cancelar Materia
# Solución de referencia

def promedio(notas):
    return sum(n * p for n, p in notas) / sum(p for n, p in notas)

def comparar_cancelacion(actual, materia, retiro=False):
    return promedio(actual) if retiro else promedio(actual + [materia])

print(comparar_cancelacion([(4, 3), (3, 2)], (2, 3), True))
