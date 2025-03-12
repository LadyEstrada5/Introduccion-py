#Primer paso 
Nombre=input("Ingrese su nommbre:")
print (f"Bienvenido/a {Nombre} al programa de pagos de la construcción de la piramide de La Sabidurìa")
#Segundo paso
Horas_Trabajo=int(input("Ingrese el número de horas trabajadas:"))
Tarifa_Hora=float(input("Ingresa la tarifa por hora:"))

#Determinar pago de horas extra
Valor_Adicional= 1.2
if Horas_Trabajo > 40:
    Horas_Extras = Horas_Trabajo - 40
    Pago_Total=(40*Tarifa_Hora)+(Horas_Extras* Tarifa_Hora *Valor_Adicional)     
    print("Se le pagaran horas extras")
else:
    Pago_Total=(Horas_Trabajo* Tarifa_Hora)
    print("No se le pagaran horas extras")
#Bonificacion   
sueldo_Brrutor=600000
bonificación=50000
if  Pago_Total > sueldo_Superior:
    Pago_Total+=bonificación
    print(f"Estimado/a {Nombre} su pago es de $ {Pago_Total:,.0f} más bonificacion de ${bonificación:,.0f}. Que tenga un excelente día")
else:
    print(f"Estimado/a {Nombre} su pago es de $ {Pago_Total:,.0f}. Que tenga un excelente día")
    
