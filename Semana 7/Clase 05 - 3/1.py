"""#Repaso de clase anterior
nota = float(input("Digite la nota: "))

if nota >= 8:
    print("Excelente")
else:
    if nota>=6: #elif funciona como una extencion del if, para seguir comprobando distintos resultados
        print("Esta bien")
    elif nota >=4:
        print("Regular")
    else:
        print("Reprobado")
"""

"""#Prueba 1
monto = float(input())

if monto > 100:
    print(f"Precio local: ${(monto + (monto*(0.07))):.2f}")
    print(f"Precio internacional: ${(monto + (monto*(0.012))):.2f}")
elif monto > 75:
    print(f"Precio local: ${(monto + (monto*(0.05))):.2f}")
    print(f"Precio internacional: ${(monto + (monto*(0.09))):.2f}")
else:
    print(f"Precio local: ${(monto + (monto*(0.00))):.2f}")
    print(f"Precio internacional: ${(monto + (monto*(0.00))):.2f}")
"""

#Prueba 2

Monto = float(input("Digite el monto: "))
Tipo = input("Tipo (local o internacional): ")

if Tipo.lower() == "local":
    if Monto > 100:
        Impuesto = 0.07
    elif Monto >75:
        Impuesto = 0.05
    else:
        Impuesto = 0
    print(f"El precio a pagar es: ${(Monto + Monto*(Impuesto)):,.2f}")            
elif Tipo.lower() == "internacional":
    if Monto >100:
        Impuesto = 0.12
    elif Monto>75:
        Impuesto = 0.09
    else:
        Impuesto = 0
    print(f"El precio a pagar es: ${(Monto + Monto*(Impuesto)):,.2f}")
else:
    print("Ese tipo no existe!!")



