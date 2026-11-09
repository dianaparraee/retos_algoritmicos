# Reto 21 - Optimización de Rutas de Entrega Nocturna
# Solución de referencia

def entregas(pedidos, limite=90):
    # pedido=(id, minutos, ganancia); estrategia didáctica: mejor ganancia por minuto
    orden = sorted(pedidos, key=lambda x: x[2] / x[1], reverse=True)
    elegidas = []
    tiempo = 0
    for p in orden:
        if tiempo + p[1] <= limite:
            elegidas.append(p)
            tiempo += p[1]
    return elegidas, sum(p[2] for p in elegidas)

print(entregas([("A", 30, 12000), ("B", 50, 18000), ("C", 20, 7000), ("D", 40, 16000)]))
