# Reto 26 - Simulador de Matrícula Sabatina vs. Nocturna
# Solución de referencia

def matricula(creditos, costo_credito, descuento=.10):
    if sum(creditos) > 18:
        return "Supera el tope de 18 créditos"
    return round(sum(creditos) * costo_credito * (1 - descuento), 2)

print(matricula([3, 3, 2, 4], 150000))
