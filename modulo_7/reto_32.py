# Reto 32 - Contador de Pasos y Distancia en Transbordos
# Solución de referencia

def pasos_distancia_calorias(tramos, longitud_m=.75):
    pasos = sum(tramos)
    km = pasos * longitud_m / 1000
    calorias = km * 60
    return pasos, round(km, 2), round(calorias, 1)

print(pasos_distancia_calorias([1200, 800, 1500]))
