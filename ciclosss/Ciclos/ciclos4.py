
suma = 0
num = 10

for n in range(num):
    numero = float(input("Ingrese un número: "))
    suma += numero

promedio = suma / num

print(f"La suma de todos los números es: {suma}")
print(f"El promedio de los números es: {promedio}")