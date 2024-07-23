import math

def es_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, math.isqrt(numero) + 1):
        if numero % i == 0:
            return False
    
    return True

numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")