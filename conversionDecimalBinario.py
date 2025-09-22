# conversion_decimal_a_binario.py - Fausto

# Pedimos el número decimal
decimal = int(input("Ingresa un número decimal: "))

# Inicializamos variables
binario = ""
n = decimal

# Condicional y repetitiva
if n == 0:
    binario = "0"
else:
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2

# Secuencial: mostrar resultado
print(f"{decimal} en binario es {binario}")