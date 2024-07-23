def multiplicar(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

lista = [8, 2, 3, -1, 7]

resultado = multiplicar(lista)

print(f"La multiplicación de los números en la lista es: {resultado}")