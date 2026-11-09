# Reto 04 - Monitoreo de Bici-parqueaderos y Batería
# Solución de referencia

def revisar_bateria(bateria, km_regreso, km_porcentaje, cupos):
    porcentaje_necesario = km_regreso * km_porcentaje
    if cupos == 0:
        return "No hay cupo: busca parqueadero alterno"
    if bateria < porcentaje_necesario:
        return "Cargar antes de regresar"
    return "Uso seguro; reserva el cupo"

print(revisar_bateria(60, 8, 5, 12))
