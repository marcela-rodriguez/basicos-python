print("Hola,ingresa los siguientes datos")

dia_nacimiento= int(input("ingresa el dia de nacimiento:"))
mes_nacimiento= int(input("ingresa el mes de nacimiento:"))
año_nacimiento= int(input("ingresa el año de nacimiento:"))
def formatear_fecha(dia_nacimiento,mes_nacimiento, año_nacimiento):
    return f"{dia_nacimiento:02d}-{mes_nacimiento:02d}-{año_nacimiento}"
print(f"su fecha de nacimiento es:{formatear_fecha(dia_nacimiento, mes_nacimiento, año_nacimiento)}")
dia_actual= int(input("ingresa el dia actual:"))
mes_actual= int(input("ingresa el mes actual:"))
año_actual= int(input("ingresa el año actual:"))
def formatear_fecha_actual(dia_actual,mes_actual, año_actual):
    return f"{dia_actual:02d}-{mes_actual:02d}-{año_actual}"
print(f"la fecha actual es:{formatear_fecha_actual(dia_actual,mes_actual,año_actual)}")
edad = año_actual - año_nacimiento
if mes_nacimiento > mes_actual:
    edad = edad -1
else:
     if mes_nacimiento == mes_actual:
        if dia_nacimiento > dia_actual:
            edad= edad -1
        if dia_actual == dia_nacimiento:
            print("Feliz cumpleaños")


print(f"su edad actual es:{edad}")