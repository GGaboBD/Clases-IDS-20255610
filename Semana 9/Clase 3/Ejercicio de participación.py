dui = input("Ingresa tu numero de dui: ")

condiciones = 0

condicion_1 = len(dui) == 10

condicion_2 = dui.count("-") == 1

posicion = dui.index("-")
condicion_3 = len(dui[posicion+1:]) == 1


if condicion_1 == True:
    condiciones +=1

if condicion_2 == True:
    condiciones +=1

if condicion_3 == True:
    condiciones +=1


print(f"Cumple {condiciones} condiciones")


### ES COMO FUNCION