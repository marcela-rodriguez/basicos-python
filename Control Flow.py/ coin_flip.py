import random

num = random.randint(0, 3)   # se genera un numero aleatorio de 0 a 3
print(f"el numero es: {num}") # se imprime la varible para ver el numero aleatorio que nos estan dando

if num > 2:
  print('Heads')
else:
  print('Tails')
