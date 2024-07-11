print("esto es calcular segundos")
total_segundos = 10000

horas = total_segundos // 3600

segundos_restantes = total_segundos % 3600

minutos = segundos_restantes // 60

segundos = segundos_restantes % 60

print(f"{total_segundos} segundos son {horas} horas, {minutos} minutos y {segundos} segundos.")
