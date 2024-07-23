
filas = int(input("Ingrese el número de filas: "))

for n in range(1, filas + 1):
    for a in range(1, n + 1):
        print("*", end="")
    print()

for n in range(filas - 1, 0, -1):
    for a in range(1, n + 1):
        print("*", end="")
    print()