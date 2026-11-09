# Reto 02 - Calculadora de Costos en Taxis vs. Plataformas
# Solución de referencia

def comparar_transportes(km, tarifa_taxi, tarifa_app, dinamica, lluvia, saldo):
    taxi = km * tarifa_taxi * (1 + lluvia)
    app = km * tarifa_app * dinamica
    opciones = {"Taxi": taxi, "Plataforma": app}
    posibles = {n: v for n, v in opciones.items() if v <= saldo}
    return min(posibles, key=posibles.get) if posibles else "Ninguna dentro del presupuesto"

print(comparar_transportes(8, 4500, 3500, 1.2, 0.10, 40000))
