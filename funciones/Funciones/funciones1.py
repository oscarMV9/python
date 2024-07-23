def max_nums(num1, num2, num3):
    max_num = num1
    
    if max_num < num2:
        max_num = num2
        
    if max_num < num3:
        max_num = num3
        
    return max_num

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

resultado = max_nums(num1, num2, num3)
print(f"El maximo entre los numeros {num1}, {num2}, {num3} es: {resultado}")