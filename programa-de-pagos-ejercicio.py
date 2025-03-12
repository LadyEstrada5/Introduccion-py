
#SISTEMA DE PAGO DE LA CONSTRUCCION DE LA PIRAMIDE:
#  salarios con bonificaciones y descuentos

    
nombre =()

while nombre!= "salir":
    nombre= input("Bienvenido al sistema de pago de la construccion de la piramide de la sabiduria\n Escriba su nombre o salir para terminar\n")

    if nombre== "salir":
     break
    tarifa_por_hora = float(input("Por favor, ingrese el valor de la tarifa por hora: "))
    horas_trabajadas = int(input("Por favor, ingrese las horas trabajadas: "))
    llegadas_tarde = int(input("¿Cuntas veces llego tarde el trabajador? "))
    
    #Si un trabajador trabaja mas de 40h las horas extra se pagan al 120%
    # si horas_trabajadas es mayor de 40 se debe multiplicar por 1.2
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        pago_normal = 40 * tarifa_por_hora
        pago_extra = horas_extras * tarifa_por_hora * 1.2
    #si no cumple la condicion se le realiza su pago normal sin pago extra
    else:
        pago_normal = horas_trabajadas * tarifa_por_hora
        pago_extra = 0
    
    sueldo_bruto = pago_normal + pago_extra
    #si el sueldo bruto es mayor a 600000 se da una bonificacion de 50000 , si no cumple la condicion bonificacion 0
    if sueldo_bruto > 600000:
        bonificacion = 50000
    else:
        bonificacion = 0
    
    descuento = 0
    #si llega tarde 3 o mas veces se le descuenta el 5% del sueldo bruto
    if llegadas_tarde >= 3:
        descuento = (sueldo_bruto * 0.05)
        
    sueldo_neto = int(sueldo_bruto + bonificacion - descuento)
    
    print(f"\nSr/Sra. {nombre}, su sueldo bruto es de {sueldo_bruto} pesos")
    print(f"Bonificación: {bonificacion} pesos")
    print(f"Descuento por tardanzas: {descuento} pesos")
    print(f"Sueldo neto a pagar: {sueldo_neto} pesos\n")