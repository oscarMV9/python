def rango(inicio, numero, final):
    if inicio <= numero <= final:
        return True
    else:
        return False

inicio = int(input("Ingrese el inicio del rango: "))
numero = int(input("Ingrese el número del rango: "))
final = int(input("Ingrese el final del rango: "))

if rango(inicio, numero, final):
    print(f"{numero} está dentro del rango ({inicio} - {final})")
else:
    print(f"{numero} está fuera del rango ({inicio} - {final})")