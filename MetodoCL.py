# Método Congruencial Lineal (LCG)

# Pedir datos al usuario
try:
    X0 = int(input("Ingresa la semilla (X0): "))
    a = int(input("Ingresa la constante multiplicativa (a): "))
    c = int(input("Ingresa la constante aditiva (c): "))
    m = int(input("Ingresa el módulo (m): "))
    n = int(input("¿Cuántos números deseas generar?: "))

    # Verificar que el módulo sea mayor que 0
    if m <= 0:
        raise ValueError("El módulo debe ser mayor que 0.")

    # Inicializar la lista y la variable de estado
    X = X0
    numeros = []

    # Generar n números pseudoaleatorios
    for i in range(n):
        X = (a * X + c) % m
        numeros.append(X)

    # Mostrar resultados
    print("\nNúmeros generados:")
    for i, num in enumerate(numeros, start=1):
        print(f"X{i} = {num}")

except ValueError as e:
    print("Error:", e)
