
filas = int(input("Ingrese el número de filas: "))

for t in range(1, filas + 1):
    for n in range(1, t + 1):
        print(f"{n} ", end="")
    print()