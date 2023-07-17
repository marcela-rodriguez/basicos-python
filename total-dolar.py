Yuan_chino= float(input("Que te queda en yuan chino? :"))

yen_japones= float(input("Que te queda en yean japones? :"))

won_surcoreano= float(input("Que te queda en won surcoreano? :"))

Yuan_chino_x_1_dolar = 6.88
yen_japones_x_1_dolar = 134.48
won_surcoreano_x_1_dolar = 1317.07

Yuan_chino_rt =(Yuan_chino / Yuan_chino_x_1_dolar)
yen_japones_rt =(yen_japones / yen_japones_x_1_dolar)
won_surcoreano_rt =(won_surcoreano / won_surcoreano_x_1_dolar)

total_dolar =(Yuan_chino_rt + yen_japones_rt + won_surcoreano_rt)
print(f"total en dolares es :{total_dolar}")
