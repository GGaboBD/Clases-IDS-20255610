nota = float(input("Digite la nota: "))

if nota >= 8:
    print("Excelente")
elif nota>=6: #elif funciona como una extencion del if, para seguir comprobando distintos resultados
    print("Esta bien")
elif nota >=4:
    print("Regular")
else:
    print("Reprobado")

