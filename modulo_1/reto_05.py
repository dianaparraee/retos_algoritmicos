# Reto 05 - Simulador de Recargo Nocturno y Horas Extras
# Solución de referencia

def salario_neto(salario_hora, diurnas, nocturnas, festivas):
    bruto = salario_hora * diurnas + salario_hora * 1.35 * nocturnas + salario_hora * 1.75 * festivas
    return round(bruto * 0.92, 2)  # Supuesto didáctico: descuento total 8%

print(salario_neto(8000, 60, 20, 4))
