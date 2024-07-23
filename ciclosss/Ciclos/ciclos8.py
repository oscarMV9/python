
filas = int(input("Ingrese el número de filas: "))
numero = 1

for n in range(1, filas + 1):
    for espacios in range(filas - n):
        print(" ", end=" ")

    for f in range(1, n + 1):
        print(numero, end=" ")
        numero += 1

    print()