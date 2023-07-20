hora=0
minutos= 0
segundos=0

print("ingresa la hora en ")

hora_i=int(input("Ingrese la hora: "))
minutos_i=int(input("Ingrese los minutos: "))
segundos_i=int(input("Ingrese los segundos: "))

if segundos_i < 59: 
    segundos=segundos_i+1
else:
   if segundos_i==59:
    segundos=00

if minutos_i < 59:
    if segundos_i==59:
        minutos=minutos_i+1
    else:
        minutos=minutos_i
else:
    if minutos_i==59:
        if segundos_i==59:
            minutos=00
        else:
            minutos=minutos_i

if hora_i<23:
    if minutos_i<59:
        if segundos_i<59:
            hora=hora_i
    
else:
    if hora_i==23:
        if minutos_i<59:
            if segundos_i<59:
                hora=hora_i
            else:
                hora=00
        else:
            if segundos_i<59:
                hora=hora_i
            else:
                hora=00



print(f" hora :{hora}")
print(f" minutos :{minutos}")
print(f" segundos :{segundos}")
    
