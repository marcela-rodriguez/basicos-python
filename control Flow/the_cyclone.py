height=int(input("¿Cual es la altura? en (cm): "))
credits=int(input("¿Cuanto credito tiene?: "))

heightR= 137
creditsR= 10

if height >= heightR and credits >= creditsR:
    print("¡Disfruta el viaje!")
elif credits>= creditsR and height< heightR:
    print("no eres lo suficiente alto para montar")
elif height>=heightR and credits<creditsR:
    print("no tienes suficiente credito")
else:
    print("no cumple ningun requisito")

