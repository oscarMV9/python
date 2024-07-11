print("calcular sueldo empleado")

sueldo_Diario = int (input("ingrese sueldo diario: "))
dias_Trab = int (input("ingrese dias trabajados: "))
total_sueldo = sueldo_Diario * dias_Trab
print("sueldo total: ", total_sueldo)

desc_Pension = total_sueldo * 0.10
print("se descuenta por pension: ", desc_Pension)
desc_Salud = total_sueldo * 0.15
print("se descuenta por salud: ", desc_Salud)

total_Pagar = total_sueldo - desc_Pension - desc_Salud

print("total a pagar: ", total_Pagar)