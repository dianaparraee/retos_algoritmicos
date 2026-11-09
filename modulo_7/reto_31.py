# Reto 31 - Evaluador del Nivel de Estrés por Carga Combinada
# Solución de referencia

def estres(respuestas):
    puntaje = sum(respuestas)
    nivel = "Bajo" if puntaje <= 6 else "Medio" if puntaje <= 12 else "Alto"
    return nivel, "Pausa activa y pedir apoyo" if nivel != "Bajo" else "Mantener hábitos"

print(estres([3, 2, 3, 1, 2]))
