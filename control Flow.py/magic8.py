import random
respuestas=["Sí definitivamente",
"Es decididamente así",
"Sin duda",
"Respuesta confusa, intenta otra vez",
"Pregunta de nuevo más tarde",
"Mejor no decirte ahora",
"Mis fuentes dicen que no",
"Las perspectivas no son tan buenas",
"Muy dudoso"]

pregunta =str(input("preguntame algo:"))
print(pregunta)

aleatoria = random.randint(1, 9)

respuesta=respuestas[aleatoria]
print(respuesta)
