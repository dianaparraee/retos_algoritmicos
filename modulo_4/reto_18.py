# Reto 18 - Planificador de Alimentación y Consumo de Cafeína
# Solución de referencia

def cafeina(mg, hora_ultima):
    alertas = []
    if mg > 400:
        alertas.append("supera 400 mg diarios")
    if hora_ultima > 20:
        alertas.append("consumo posterior a las 8 p.m.")
    return alertas or ["dentro de los límites del ejercicio"]

print(cafeina(450, 21))
