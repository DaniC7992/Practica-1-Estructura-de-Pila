
CAPACIDAD_MAX = 8
pila = [None] * CAPACIDAD_MAX
TOPE = 0 

def mostrar_pila():
    print("PILA:", pila)
    print("TOPE =", TOPE)
    print("------")

print("Estado inicial:")
mostrar_pila()

if TOPE < CAPACIDAD_MAX:
    pila[TOPE] = "X"
    TOPE += 1
    print("a) Insertar (PILA, X)")
else:
    print("a) Error: Desbordamiento")
mostrar_pila()


if TOPE < CAPACIDAD_MAX:
    pila[TOPE] = "Y"
    TOPE += 1
    print("b) Insertar (PILA, Y)")
else:
    print("b) Error: Desbordamiento")
mostrar_pila()


if TOPE > 0:
    TOPE -= 1
    Z = pila[TOPE]
    pila[TOPE] = None
    print(f"c) Eliminar (PILA, Z) → Z = {Z}")
else:
    print("c) Error: Subdesbordamiento")
mostrar_pila()

if TOPE > 0:
    TOPE -= 1
    T = pila[TOPE]
    pila[TOPE] = None
    print(f"d) Eliminar (PILA, T) → T = {T}")
else:
    print("d) Error: Subdesbordamiento")
mostrar_pila()


if TOPE > 0:
    TOPE -= 1
    U = pila[TOPE]
    pila[TOPE] = None
    print(f"e) Eliminar (PILA, U) → U = {U}")
else:
    print("e) Error: Subdesbordamiento (pila vacía)")
mostrar_pila()


if TOPE < CAPACIDAD_MAX:
    pila[TOPE] = "V"
    TOPE += 1
    print("f) Insertar (PILA, V)")
else:
    print("f) Error: Desbordamiento")
mostrar_pila()


if TOPE < CAPACIDAD_MAX:
    pila[TOPE] = "W"
    TOPE += 1
    print("g) Insertar (PILA, W)")
else:
    print("g) Error: Desbordamiento")
mostrar_pila()


if TOPE > 0:
    TOPE -= 1
    p = pila[TOPE]
    pila[TOPE] = None
    print(f"h) Eliminar (PILA, p) → p = {p}")
else:
    print("h) Error: Subdesbordamiento")
mostrar_pila()


if TOPE < CAPACIDAD_MAX:
    pila[TOPE] = "R"
    TOPE += 1
    print("i) Insertar (PILA, R)")
else:
    print("i) Error: Desbordamiento")
mostrar_pila()

print("RESULTADOS FINALES")
print("Pila final:", pila)
print("TOPE final =", TOPE)
print("La pila quedó con", TOPE, "elementos.")

if TOPE <= CAPACIDAD_MAX:
    print("No hubo desbordamiento.")
print("Hubo un caso de subdesbordamiento en la operación (e) porque la pila estaba vacía.")
