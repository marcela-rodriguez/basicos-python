pesos=float(input("Cuanto tienes en pesos colombianos? "))
soles=float(input("Cuanto tienes en soles peruanos? "))
reales=float(input("Cuanto tienes en reales brasileños? "))

peso_a_1_dolar=0.00025
sol_a_1_dolar= 0.27
real_a_1_dolar=0.20

pesos_colombianos=(pesos*peso_a_1_dolar)
soles_peruanos=(soles*sol_a_1_dolar)
reales_brasileños=(reales*real_a_1_dolar)

total_dolares=(pesos_colombianos + soles_peruanos + reales_brasileños)
print(f"el total en dolares es: {total_dolares}")

"""
pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

total = pesos * 0.00025 + soles * 0.28 + reais * 0.21

print(total)"""