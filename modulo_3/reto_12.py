# Reto 12 - Optimizador de Micro-tiempos de Estudio en el Bus
# Solución de referencia

def mochila_tiempo(items, minutos):
    # items = [(nombre, duración, valor)]
    mejor = (0, [])
    for mascara in range(1 << len(items)):
        elegidos = [items[i] for i in range(len(items)) if mascara >> i & 1]
        if sum(x[1] for x in elegidos) <= minutos and sum(x[2] for x in elegidos) > mejor[0]:
            mejor = (sum(x[2] for x in elegidos), [x[0] for x in elegidos])
    return mejor

print(mochila_tiempo([("Lectura", 30, 5), ("Audio", 20, 4), ("Video", 40, 8)], 60))
