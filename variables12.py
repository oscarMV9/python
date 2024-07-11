print("sacando la hipotenusa")
import math

cateto1 = int(input("ingrese el lado del cateto: "))
cateto2 = int(input("ingrese el segundo lado: "))

R_cateto1 = cateto1 * cateto1
R_cateto2 = cateto2 * cateto2

R_sumaCatetos = R_cateto1 + R_cateto2

raiz_cuadrada = math.sqrt(R_sumaCatetos)

print(f"el cateto es {raiz_cuadrada:.4f}")



