import datetime
import random

registros = []

opcion_menu = 0
while(opcion_menu != 3):
    print("""
    MENU
    1. Agregar
    2. Mostrar 
    3. salir
    """)
    opcion_menu = int(input("Ingrese una opcion del menú: "))

    if opcion_menu == 1:
        print("ingrese los siguientes datos")
        nombre=str(input("nombre: "))
        cedula=int(input("cedula: "))
        fecha_de_nacimiento=input("fecha de nacimiento: ")
        correo=str(input("correo: "))
        ciudad_de_recidencia=str(input("ciudad de recidencia: "))
        ciudad_de_origen=str(input("ciuda de origen: "))
        artista=str(input("Artista favorito: "))
        print("ingrese tres canciones favoritas:")
        cancion1=str(input("cancion 1: "))
        cancion2=str(input("cancion 2: "))
        cancion3=str(input("cancion 3: "))

        persona = {
            "nombre": nombre,
            "cedula": cedula,
            "fecha de nacimiento":fecha_de_nacimiento,
            "correo electronico":correo,
            "ciuda de recidencia":ciudad_de_recidencia,
            "ciuda de origen":ciudad_de_origen,
            "artista":artista,
            "cancion 1": cancion1,
            "cancion 2": cancion2,
            "cancion 3": cancion3
        }
        registros.append(persona)


    if opcion_menu == 2:
        posicion=int(input("ingrese la posicion:"))
        registros[posicion]
        print(registros[posicion])
        
        


