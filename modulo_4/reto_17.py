# Reto 17 - Gestión de Parqueaderos de Motos y Carros
# Solución de referencia

def parqueadero(cap_motos, ocup_motos, cap_carros, ocup_carros, tipo, horas):
    disponible = (ocup_motos < cap_motos) if tipo == "moto" else (ocup_carros < cap_carros)
    tarifa = (1000 if tipo == "moto" else 2000) * horas
    return disponible, tarifa * .8  # 20% descuento nocturno estudiantil

print(parqueadero(50, 49, 20, 10, "moto", 3))
