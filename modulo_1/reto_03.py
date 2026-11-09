# Reto 03 - Validador de Subsidio y Tarjeta TuLlave (SITP)
# Solución de referencia

def validar_tullave(saldo, tipo_usuario, minutos):
    subsidio = {"Estándar": 0, "Sisbén": 500}.get(tipo_usuario, 0)
    costo = max(0, 2950 - subsidio)
    transbordo = minutos <= 110
    return {"puede_viajar": saldo >= costo or transbordo,
            "requiere_recarga": saldo < costo and not transbordo,
            "saldo_final_estimado": saldo if transbordo else saldo - costo}

print(validar_tullave(2500, "Sisbén", 40))
