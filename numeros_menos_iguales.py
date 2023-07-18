print("ingrese 20 numeros: ")
lista_numero=[]

for i in range(0,20):
    numero=int(input("numero: "))
    lista_numero.append(numero)

for numero in lista_numero:    
    if numero <= 25:
        print(f"el numero es menor o iagual que 25 :{numero}")
    

