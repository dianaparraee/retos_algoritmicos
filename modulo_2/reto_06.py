# Reto 06 - Presupuesto Quincenal del Estudiante-Trabajador
# Solución de referencia

def presupuesto(ingreso, gastos_diarios, pasaje_diario, dia=10):
    saldo = ingreso - sum(gastos_diarios[:dia])
    dias_restantes = 15 - dia
    necesario = dias_restantes * pasaje_diario
    return saldo, necesario, saldo >= necesario

print(presupuesto(900000, [25000] * 15, 6500))
