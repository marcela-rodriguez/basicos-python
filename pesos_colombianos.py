print("ingrese el precio de las camisas en dolares")
total_suma=0
valor_colombiano=4000
for i in range(0,5):
    dolar=int(input("ingrese el precio en dolar: "))
    total_suma=total_suma+dolar

total_compra=total_suma*valor_colombiano
print(f"El total de la venta es $ {total_compra} pesos")
#el codigo se crea sin la variable listas 