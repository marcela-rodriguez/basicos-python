tabla=0
numero=int(input("ingrese un numero : "))
for i in range(10,0,-1):
    tabla=numero*i
    print(f"{numero} x {i} = {tabla}")
