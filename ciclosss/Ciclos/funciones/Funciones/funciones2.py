import math

def menu():
    menu_text = """Ingrese la figura que desea calcular: 
    1. Circulo
    2. Cuadrado
    3. Rectangulo
    4. Triangulo
    5. Salir
    """
    print(menu_text)
    
    opcion = input("Ingrese su opción: ")
    return opcion

def circulo(radio):
    pi = math.pi
    area = pi * (radio ** 2)
    return area

def cuadrado(lado):
    area = lado ** 2
    return area

def rectangulo(base, altura):
    area = base * altura
    return area

def triangulo(base, altura):
    area = (base * altura) / 2
    return area

while True:
    opcion = menu()
    
    if opcion == '1':
        radio = float(input("Ingrese el radio del círculo: "))
        print(f"El área del círculo es: {circulo(radio)}")
    elif opcion == '2':
        lado = float(input("Ingrese el lado del cuadrado: "))
        print(f"El área del cuadrado es: {cuadrado(lado)}")
    elif opcion == '3':
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print(f"El área del rectángulo es: {rectangulo(base, altura)}")
    elif opcion == '4':
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print(f"El área del triángulo es: {triangulo(base, altura)}")
    elif opcion == '5':
        print("¡Adios, por favor no vuelva!")
        break
    else:
        print("Ingrese una opción válida, por favor.")
