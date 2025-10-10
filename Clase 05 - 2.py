#EJERCICIO 1
Enero = int(input("Ingrese la cantidad producida en enero: "))
Febrero = int(input("Ingrese la cantidad producida en febrero: "))
Marzo = int(input("Ingrese la cantidad producida en marzo: "))


print("Las cantidades producidas en el primer trimestre del año son:")
print(f" - Enero: {Enero}")
print(f" - Febrero: {Febrero}")
print(f" - Marzo: {Marzo}")
print(f"Y el costo total de esos tres meses es de : ${(Enero*1.25) + (Febrero*1.38)+ (Marzo*1.14):.2f}")



#Ejercicio 2
#Crear una lista con los 5 dias de la semana en español

Dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

Lu = int(input("Ingresa la cantidad producida el Lunes: "))
Dias[0] = Lu
print(Dias)
Mar = int(input("Ingresa la cantidad producida el Martes: "))
Dias[1] = Mar
print(Dias)
Mier = int(input("Ingresa la cantidad producida el Miercoles: "))
Dias[2] = Mier
print(Dias)
Jue = int(input("Ingresa la cantidad producida el Jueves: "))
Dias[3] = Jue
print(Dias)
Vier = int(input("Ingresa la cantidad producida el Viernes: "))
Dias[4] = Vier
print(Dias)

print(f"La produccion de la semana fue de: {Lu+Mar+Mier+Jue+Vier} unidades")



#EJERCICIO 4
#Crear una coleccion de los nombres de 7 alumnos en el orden en el cual entraron al aula y debe mostrar ese orden

alumnos = ("Diego", "Franquito", "Calvito", "Aby", "Alvin", "Medranito", "Genesis")

niño = int(input("Ingrese el orden del niño que desea saber (1-7): "))


print(f"El alumno que ingreso como numero {niño} es {alumnos[niño-1]}")



#EJERCICIO 5
#Capturar nombre y apellidos 

Nombre = input("Escribe tu primer nombre: ")
Apellido = input("Escribe tu primer apellido: ")

print(f"{Nombre.lower()}.{Apellido.lower()}@ISND.com") #.lower es para hacer las cosas minusculas
print(f"{Nombre.lower()[0]}.{Apellido.lower()}@ISND.com")


#EJERCICIO 6
Salario_usuario = input("Ingrese su salario: ")


print(f"El valor ingresado cuenta con un signo de dolar al inicio? {"$" in Salario_usuario[0]}")
print(f"El valor ingresado cuenta con un solo signo de dolar? {Salario_usuario.count("$")==1}")


Texto_Incriptado = "DFGUPCCBJKAJ"

primera_letra = Texto_Incriptado[0]
print(f"{Texto_Incriptado[0::3]}")
