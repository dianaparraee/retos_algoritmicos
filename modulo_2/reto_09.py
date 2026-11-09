# Reto 09 - Calculadora de Nota Mínima Requerida (Tercer Corte)
# Solución de referencia

def nota_tercer_corte(nota1, nota2, minima=3.0):
    necesaria = (minima - nota1 * .30 - nota2 * .30) / .40
    return max(0, necesaria), necesaria <= 5

print(nota_tercer_corte(3.2, 2.8))
