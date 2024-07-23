
num = int(input("Ingrese los numeros de la serie Fibonacchi: "))

if num <= 0:
    print("Ingrese un numero valido.")

else:
    num1, num2 = 0, 1
    fibonacci_terms = []
    suma_f = 0

    for numero in range(num):
        fibonacci_terms.append(num1)
        suma_f += num1
        num1, num2 = num2, num1 + num2

    print(f"Los primeros {num} de la serie Fibonacci son: ", fibonacci_terms)
    print("La suma de los primeros", num, "de la serie fibonacci son: ", suma_f)