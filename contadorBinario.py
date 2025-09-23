# contador_binario.py

# Pedimos el límite al usuario

limite = int(input("Ingresa hasta qué número quieres contar en binario: "))
print("=== Contador Binario ===")

# Repetitiva: usamos un ciclo while
i = 0

while i <= limite:
    # Secuencial: mostramos decimal y binario usando condicionales si queremos formato
    binario = ""
    n = i
    if n == 0:
        binario = "0"
    else:
        while n > 0:  # repetitiva
            binario = str(n % 2) + binario
            n = n // 2
    print(f"{i} en binario es {binario}")
    i += 1
    

# conversion_decimal_a_binario.py 

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