# Reto 27 - Validador de Prerrequisitos del Plan de Estudios
# Solución de referencia

def materias_habilitadas(aprobadas, materias):
    return [nombre for nombre, requisitos in materias.items() if set(requisitos) <= set(aprobadas)]

print(materias_habilitadas(["Python I", "Matemáticas"], {"Python II": ["Python I"], "Algoritmos": ["Python I", "Matemáticas"], "BD": ["Redes"]}))
