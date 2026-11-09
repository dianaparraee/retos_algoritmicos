# Reto 30 - Control de Hidratación en la Jornada Continua
# Solución de referencia

def hidratacion(peso, ingestas):
    meta = peso * 35
    total = sum(ingestas)
    return meta, total, round(total / meta * 100, 1)

print(hidratacion(70, [500, 400, 600]))
