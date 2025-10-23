# Método del Cuadrado Medio - versión simple (semilla de 4 dígitos)

# Pedir semilla y cantidad
semilla = input("Ingresa una semilla : ").strip()
if not (semilla.isdigit() and len(semilla) == 4):
    raise SystemExit("La semilla debe ser un número de 4 dígitos.")

semilla = int(semilla)
n = int(input("¿Cuántos números deseas generar?: "))

print("\n--- Método del Cuadrado Medio ---")
for i in range(n):
    cuadrado = semilla ** 2
    cuadrado_str = str(cuadrado).zfill(8)   # asegura 8 dígitos
    medio_str = cuadrado_str[2:6]          # 4 dígitos centrales
    medio = int(medio_str)
    numero = medio / 10000.0               # normalizado en [0,1)
    print(f"{i+1}. Cuadrado: {cuadrado_str} -> Medio: {medio_str} -> R: {numero:.4f}")
    semilla = medio
