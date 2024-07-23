def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

numero = int(input("Ingrese el número del cual desea calcular el factorial: "))
print(f"El factorial de {numero} es: {factorial(numero)}")