print("Se analiza el año bisisesto")

año_actual=int(input("ingrese el año actual: "))
residuo_division = año_actual % 4
if residuo_division == 0 :
    print("es año bisiesto")
else:
    print("no es año bisiesto")
