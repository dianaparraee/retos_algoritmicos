# Reto 35 - Validador de Identidad y Control de Acceso
# Solución de referencia

def acceso(documento, matriculados, fallos):
    if documento in matriculados:
        return "Acceso permitido", fallos
    return "Acceso denegado", fallos + 1

print(acceso("123", {"123", "456"}, 0))
