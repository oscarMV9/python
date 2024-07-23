def sumar(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

lista = [8, 2, 3, 0, 7]

resultado = sumar(lista)

print(f"La suma de los números en la lista es: {resultado}")