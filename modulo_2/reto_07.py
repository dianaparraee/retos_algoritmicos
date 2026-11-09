# Reto 07 - Vaca Virtual para Proyectos de Aula
# Solución de referencia

def vaca_virtual(meta, aportes):
    total = sum(aportes)
    diferencia = meta - total
    if diferencia > 0:
        return {"faltante": diferencia, "pendientes": [i + 1 for i, a in enumerate(aportes) if a == 0]}
    return {"faltante": 0, "excedente": -diferencia, "aporte_por_persona": total / len(aportes)}

print(vaca_virtual(200000, [50000, 30000, 0, 50000]))
