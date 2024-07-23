def es_palindromo(cadena):
    cadena_invertida = cadena[::-1]

    if cadena == cadena_invertida:
        print("La frase es un palíndromo.")
        return True
    else:
        print("La frase no es un palíndromo.")
        return False

frase = input("Ingrese la frase para verificar: ")
es_palindromo(frase)