total=0   
opcion_menu = 0

while(opcion_menu != 2):
    print("""
    MENU
    1. registrar consumo
    2. salir
    """)
    opcion_menu = int(input("Ingrese una opcion del menú: "))
    if opcion_menu == 1:
        compra=int(input("registar el consumo realizado por el cliente: "))
        if compra>50000 :
            compra_descuento= compra*20/100
            pagar=compra-compra_descuento
            print(f"El descuento del 20% es:{compra_descuento}")
            print(f"El total a pagar es {pagar}")
            total=total+pagar
        else:
            print(f"El total a pagar es:{compra}")
            total=total+compra
            
            
        print(f"total ventas :{total}") 
