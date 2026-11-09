"""Proyecto final - Reto 05: Simulador de Recargo Nocturno y Horas Extras.

Aplicación de consola con menú, validación de entradas, funciones separadas
y al menos cinco pruebas (casos de prueba).
"""

# ---------- Funciones de cálculo ----------

def calcular_salario_bruto(salario_hora, diurnas, nocturnas, festivas):
    """Calcula el salario bruto aplicando recargos nocturno (35%) y festivo (75%)."""
    return (salario_hora * diurnas
            + salario_hora * 1.35 * nocturnas
            + salario_hora * 1.75 * festivas)


def calcular_salario_neto(salario_hora, diurnas, nocturnas, festivas, descuento=0.08):
    """Calcula el salario neto aplicando descuento de ley (8% por defecto)."""
    bruto = calcular_salario_bruto(salario_hora, diurnas, nocturnas, festivas)
    return round(bruto * (1 - descuento), 2)


def resumen_pago(salario_hora, diurnas, nocturnas, festivas):
    """Devuelve un diccionario con el desglose del pago."""
    bruto = calcular_salario_bruto(salario_hora, diurnas, nocturnas, festivas)
    neto = calcular_salario_neto(salario_hora, diurnas, nocturnas, festivas)
    return {
        "horas_diurnas": diurnas,
        "horas_nocturnas": nocturnas,
        "horas_festivas": festivas,
        "salario_bruto": round(bruto, 2),
        "descuento_ley": round(bruto * 0.08, 2),
        "salario_neto": neto,
    }


# ---------- Validación de datos ----------

def leer_numero(mensaje, tipo=float, minimo=0):
    """Lee un número del usuario validando que sea numérico y no negativo."""
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = tipo(entrada)
        except ValueError:
            print("  Error: ingrese un valor numérico válido.")
            continue
        if valor < minimo:
            print(f"  Error: el valor debe ser mayor o igual a {minimo}.")
            continue
        return valor


def validar_horas(diurnas, nocturnas, festivas, tope=240):
    """Valida que el total de horas no supere un tope razonable (240 quincenales)."""
    total = diurnas + nocturnas + festivas
    if total > tope:
        return False, f"Total de horas ({total}) supera el tope de {tope}."
    if total == 0:
        return False, "Debe ingresar al menos una hora trabajada."
    return True, "OK"


# ---------- Menú ----------

def mostrar_menu():
    print("\n===== SIMULADOR DE RECARGO NOCTURNO =====")
    print("1. Calcular salario quincenal")
    print("2. Ejecutar pruebas (5 casos)")
    print("3. Salir")
    return input("Seleccione una opción: ").strip()


def opcion_calcular():
    print("\n--- Ingreso de datos ---")
    salario_hora = leer_numero("Salario por hora: ", float, 0)
    diurnas = leer_numero("Horas diurnas: ", float, 0)
    nocturnas = leer_numero("Horas nocturnas (después de 7 p.m.): ", float, 0)
    festivas = leer_numero("Horas festivas: ", float, 0)

    ok, msg = validar_horas(diurnas, nocturnas, festivas)
    if not ok:
        print("  Validación fallida:", msg)
        return

    resultado = resumen_pago(salario_hora, diurnas, nocturnas, festivas)
    print("\n--- Resultado ---")
    for clave, valor in resultado.items():
        print(f"  {clave}: {valor}")


def opcion_pruebas():
    ejecutar_pruebas()


# ---------- Pruebas (5 casos) ----------

def ejecutar_pruebas():
    casos = [
        # (salario_hora, diurnas, nocturnas, festivas, neto_esperado)
        (8000, 60, 20, 4, 691840.0),   # caso base del curso
        (10000, 80, 0, 0, 736000.0),   # solo diurnas
        (9000, 0, 40, 0, 447120.0),    # solo nocturnas
        (7500, 0, 0, 10, 120750.0),    # solo festivas
        (8500, 30, 10, 5, 408595.0),   # mixto
    ]

    print("\n--- Ejecución de 5 casos de prueba ---")
    # Encabezado de la tabla
    print(f"{'Caso':>5} {'Sal/Hora':>10} {'Diurnas':>9} {'Nocturnas':>11} "
          f"{'Festivas':>9} {'Bruto':>12} {'Neto':>12} {'Esperado':>12} {'Estado':>7}")
    print("-" * 90)

    todas_ok = True
    for i, (sh, d, n, f, esperado) in enumerate(casos, start=1):
        bruto = calcular_salario_bruto(sh, d, n, f)
        obtenido = calcular_salario_neto(sh, d, n, f)
        estado = "OK" if abs(obtenido - esperado) < 0.01 else "FALLO"
        if estado == "FALLO":
            todas_ok = False
        print(f"{i:>5} {sh:>10} {d:>9} {n:>11} {f:>9} "
              f"{round(bruto, 2):>12} {obtenido:>12} {esperado:>12} {estado:>7}")

    print("-" * 90)
    print("Resultado global:", "TODAS LAS PRUEBAS OK" if todas_ok else "HAY FALLOS")

    # Notas: valores base fijos utilizados en los cálculos
    print("\n--- Notas / Valores base ---")
    print("  Recargo nocturno (después de 7 p.m.): +35% sobre el salario por hora")
    print("  Recargo festivo: +75% sobre el salario por hora")
    print("  Descuento de ley aplicado al bruto: 8%")
    print("  Fórmula: bruto = (H_diurnas + 1.35*H_nocturnas + 1.75*H_festivas) * salario_hora")
    print("  Neto = bruto * (1 - 0.08)")


def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            opcion_calcular()
        elif opcion == "2":
            opcion_pruebas()
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    # Ejecución de los 5 casos de prueba al iniciar
    # ejecutar_pruebas()
    # Luego se ofrece el menú interactivo
    main()
