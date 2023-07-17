print("calcular el tiempo en minutos por kilometro ")
kilometros= float(input("ingrese los kilometros:"))
horas=int(input("ingrese las horas:"))
minutos=int(input("ingrese los minutos:"))
horas_en_minutos= horas * 60 + minutos
tiempo= horas_en_minutos/kilometros
print(f"el tiempo calculado es:{tiempo} en minutos por kilometro")
