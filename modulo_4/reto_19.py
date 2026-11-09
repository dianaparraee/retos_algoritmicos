# Reto 19 - Cálculo de Huella de Carbono del Desplazamiento
# Solución de referencia

def huella_km(trayectos, semanas=1):
    factores = {"bus": 0.10, "moto": 0.12, "carro": 0.21, "bici": 0, "caminar": 0}
    return sum(km * factores.get(m, 0) for m, km in trayectos) * semanas

print(huella_km([("bus", 80), ("moto", 20)]))
