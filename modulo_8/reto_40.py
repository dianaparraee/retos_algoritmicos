# Reto 40 - Eficiencia de Vehículo / Moto en Tráfico Bogotano
# Solución de referencia

def eficiencia(km, galones, costo_galon, pasaje_transmilenio, viajes):
    rendimiento = km / galones
    costo_transporte = galones * costo_galon
    costo_tm = pasaje_transmilenio * viajes
    return rendimiento, costo_transporte, costo_tm

print(eficiencia(120, 4, 16000, 2950, 10))
