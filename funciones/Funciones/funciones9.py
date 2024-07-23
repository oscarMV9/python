def elementos_unicos(lista):
    lista_unicos = []
    for elemento in lista:
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)
    return lista_unicos

print("Ingrese los valores de la lista separados por espacios: ")
entrada = input()
lista_ejemplo = entrada.split()

lista_resultado = elementos_unicos(lista_ejemplo)

print("Lista con elementos únicos: [", end="")
for index, elemento in enumerate(lista_resultado):
    print(elemento, end="")
    if index < len(lista_resultado) - 1:
        print(", ", end="")
print("]")