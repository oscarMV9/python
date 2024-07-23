
altura = int(input("Ingrese la altura de la 'Z': "))

for a in range(1, altura + 1):
    if a == 1 or a == altura:
        for z in range(1, altura + 1):
            print("*", end="")
    else:
        for z in range(altura - a):
            print(" ", end="")
        print("*")
    print()