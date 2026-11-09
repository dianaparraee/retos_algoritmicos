# Reto 34 - Registro y Clasificación de Incidencias en Campus
# Solución de referencia

def incidencias_nocturnas(incidentes):
    return [i for i in incidentes if 20 <= int(i["hora"].split(":")[0]) < 23 or (int(i["hora"].split(":")[0]) == 23 and int(i["hora"].split(":")[1]) <= 30)]

print(incidencias_nocturnas([{"evento": "hurto", "hora": "21:10", "sector": "A"}, {"evento": "caída", "hora": "18:00", "sector": "B"}]))
