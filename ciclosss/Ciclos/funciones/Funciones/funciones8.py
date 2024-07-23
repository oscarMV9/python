def contador_mayusculas_minusculas(cadena):
    contador_mayusculas = 0
    contador_minusculas = 0

    for caracter in cadena:
        if caracter.isupper():
            contador_mayusculas += 1
        elif caracter.islower():
            contador_minusculas += 1

    return contador_mayusculas, contador_minusculas

cadena = input("Ingrese una cadena: ")

mayusculas, minusculas = contador_mayusculas_minusculas(cadena)

print(f"Número de mayúsculas: {mayusculas}")
print(f"Número de minúsculas: {minusculas}")