print("ingrese el precio de las camisas en dolares")
dolarlista=[]
total_suma=0
for i in range(0,5):
    dolar=int(input("ingrese el precio en dolar: "))
    dolarlista.append(dolar)
    total_suma= sum(dolarlista)

valor_colombiano = 4000
venta_ropa=total_suma * valor_colombiano

print(f"El total de la venta es $ {venta_ropa} pesos")
