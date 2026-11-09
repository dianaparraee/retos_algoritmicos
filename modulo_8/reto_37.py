# Reto 37 - Simulador de Arriendo Compartido entre Estudiantes
# Solución de referencia

def arriendo(canon, servicios, habitaciones):
    total = canon + servicios
    area_total = sum(habitaciones.values())
    return {n: round(total * area / area_total, 2) for n, area in habitaciones.items()}

print(arriendo(1200000, 300000, {"Ana": 12, "Luis": 10, "Marta": 8}))
