# Reto 33 - Simulador de Batería y Ahorro para Emergencias
# Solución de referencia

def bateria_emergencia(bateria, minutos_viaje, consumo_por_minuto):
    necesaria = minutos_viaje * consumo_por_minuto
    return bateria >= necesaria, ["GPS", "Datos móviles"] if bateria < necesaria else []

print(bateria_emergencia(30, 90, .4))
