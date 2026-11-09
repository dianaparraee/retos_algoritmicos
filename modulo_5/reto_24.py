# Reto 24 - Planificador de Turnos para Call Center Nocturno
# Solución de referencia

def turno_valido(fin_turno, inicio_clase, descanso_min=360):
    # horas en formato decimal; permite cruzar medianoche
    if inicio_clase < fin_turno:
        inicio_clase += 24
    return inicio_clase - fin_turno >= descanso_min / 60

print(turno_valido(6, 13))
