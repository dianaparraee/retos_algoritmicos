# Reto 36 - Calculadora de Costos por Pérdida de Objetos
# Solución de referencia

def perdida(objetos):
    total = sum(valor for nombre, valor in objetos)
    prioridad = sorted(objetos, key=lambda x: x[1], reverse=True)
    return total, prioridad

print(perdida([("cuaderno", 30000), ("celular", 900000), ("carné", 15000)]))
