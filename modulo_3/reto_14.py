# Reto 14 - Sistema de Red de Apoyo / Paradero Seguro
# Solución de referencia

def agrupar_por_destino(estudiantes):
    grupos = {}
    for nombre, destino, hora in estudiantes:
        grupos.setdefault((destino, hora), []).append(nombre)
    return {k: v for k, v in grupos.items() if len(v) >= 2}

print(agrupar_por_destino([("Ana", "Portal Norte", "21:30"), ("Luis", "Portal Norte", "21:30"), ("Marta", "Portal Sur", "21:30")]))
