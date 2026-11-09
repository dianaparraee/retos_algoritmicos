# Reto 15 - Simulador de Reporte de Extravío de Documentos
# Solución de referencia

def pasos_extravio(objetos):
    pasos = []
    costo = 0
    if "tarjeta" in objetos:
        pasos += ["bloquear tarjeta"]
        costo += 8000
    if "cedula" in objetos:
        pasos += ["denunciar pérdida", "solicitar duplicado"]
        costo += 55000
    if "carne" in objetos:
        pasos += ["avisar a la universidad", "pedir reexpedición"]
        costo += 15000
    return pasos, costo

print(pasos_extravio(["tarjeta", "carne"]))
