# Reto 11 - Alerta de Inasistencia (Regla del 20%)
# Solución de referencia

def alerta_inasistencia(horas_clase, horas_faltadas, limite=.20):
    porcentaje = horas_faltadas / horas_clase
    restantes = max(0, int(horas_clase * limite) - horas_faltadas)
    return porcentaje, restantes, porcentaje >= limite

print(alerta_inasistencia(64, 8))
