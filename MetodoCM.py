# Método Congruencial Multiplicativo (MCG)
# Fórmula: X_{n+1} = (a * X_n) mod m

# Pedir los datos al usuario
X0 = int(input("Ingresa la semilla : "))
a = int(input("Ingresa la constante multiplicativa (a): "))
m = int(input("Ingresa el módulo (m): "))
n = int(input("¿Cuántos números deseas generar?: "))

# Verificar que la semilla no sea cero
if X0 == 0:
    print("La semilla no puede ser 0. Intenta con otro valor.")
else:
    X = X0
    print("\nNúmeros generados:")
    for i in range(n):
        X = (a * X) % m
        print(f"X{i+1} = {X}")
    

