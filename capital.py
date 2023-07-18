capital_inicial=float(input("ingrese su capital: "))
intereses=float(input("ingrese la tasa de interes anual :"))
años=0
capital=capital_inicial
while capital_inicial*2>=capital:
    ganancias= capital * intereses /100
    capital= capital + ganancias
    años=años+1
print (f"El capital se duplica en: {años} años")
