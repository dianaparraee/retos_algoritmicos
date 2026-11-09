# Reto 10 - Detector de Cruce de Horarios y Disponibilidad
# Solución de referencia

def coincidencias(disponibilidades, minimo=3):
    # Cada disponibilidad es una lista de franjas, por ejemplo ["18-19", "19-20"]
    todas = set().union(*map(set, disponibilidades))
    return sorted(f for f in todas if sum(f in d for d in disponibilidades) >= minimo)

print(coincidencias([["18-19", "19-20"], ["18-19"], ["18-19", "20-21"], ["17-18", "18-19"]]))
