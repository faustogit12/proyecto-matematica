import random


def binario_a_decimal(): ## funcion de binario a decimal
    binario = input("Ingrese un numero binario (Solo 0 y 1): \n")

    # valido que solo se carguen 0 y 1
    for c in binario:
        if c != '0' and c != '1':
            print("Error: Solo se permiten 0 y 1.\n")
            input("Presiona enter para volver.\n")
            return

    decimal = 0
    longitud = len(binario)

    #Conversion a decimal
    for i in range(longitud):
        bit = int(binario[i])
        potencia = longitud - i - 1
        decimal += bit * (2 ** potencia)

    print(f"\nBinario: {binario}  ---> Decimal: {decimal}\n" )
    input("Presiona enter para volver.\n")

def juego_adivinanza():

    print("\n=== Juego de adivinanza binaria ===\n")

    numero = random.randint(0,15)   ## el numero aleatorio
    binario = bin(numero)[2:].zfill(4) # lo muestro en binario con 4 bits
    print(f"Adivina el numero decimal de este binario: {binario}")

    intento = input("Tu respuesta: ")

    #validacion 

    if not intento.isdigit():
        print("Error: debes ingresar un numero entero")
        input("Presiona enter para volver.")
        return
    #respuesta
    if int(intento) == numero:
        print("Correcto! Acertaste el numero.")
    else:
        print(f"Incorrecto, el numero era: {numero}")

    input("Presiona enter para volver \n")








##MENU

while True:
    print("\n=== Menu de opciones ===\n")
    print("1 - Contador Binario 0 a 15\n")
    print("2 - Convertir decimal a binario\n")
    print("3 - Convertir binario a decimal\n")
    print("4 - Juego de advinanza binaria\n")
    print("5 - Salir\n")
    opcion = input("Seleccione una opcion (1-5): \n")

    if opcion == "4":
        juego_adivinanza()
