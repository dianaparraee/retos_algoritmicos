# Reto 01 - Optimizador de Ruta TransMilenio en Hora Pico
# Solución de referencia (curso "Python desde cero: 40 retos universitarios")

def ruta_tm(hora_salida, minutos_base, expreso=False):
    hora = int(hora_salida.split(":")[0])
    pico = 16 <= hora < 20
    tiempo = minutos_base * (1.25 if pico else 1)
    tipo = "expresa" if expreso else "fácil"
    return round(tiempo), tipo

print(ruta_tm("17:30", 55, True))
