print("sacar el valor de IVA en una compra")

Nombre_produc = str (input("ingrese nombre del producto: "))
valor_Unit = int (input("ingrese la cantidad unitaria del producto: "))
Unidades = int (input("ingrese la cantididad de productos: "))

valor_SinIva = valor_Unit * Unidades

print("el valor total sin IVA: ", valor_SinIva)

valor_IVA = valor_SinIva * 0.19
valor_total = valor_SinIva + valor_IVA

print("total pagar: ", valor_total)