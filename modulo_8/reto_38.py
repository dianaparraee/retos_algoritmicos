# Reto 38 - Cálculo de Consumo de Datos en Clases Híbridas
# Solución de referencia

def agotamiento_datos(paquete_gb, consumo_hora_gb, horas_diarias, dias_mes=30):
    consumo_dia = consumo_hora_gb * horas_diarias
    dia = paquete_gb / consumo_dia
    return min(dias_mes, int(dia) + 1), consumo_dia

print(agotamiento_datos(20, .7, 2))
