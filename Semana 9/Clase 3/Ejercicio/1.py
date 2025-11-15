dui = input("Ingrese su numero de DUI: ")


def verificacion_DUI(dui):
    condiciones_cumplidas = 0

    if len(dui) == 10:
        condiciones_cumplidas +=1
    else:
        condiciones_cumplidas +=0
    
    if dui.count("-") == 1:
        condiciones_cumplidas +=1
    else:
        condiciones_cumplidas +=0

    if "-" in dui:
        posicion = dui.index("-")
        if len(dui[posicion+1:]) == 1:
            condiciones_cumplidas +=1
        else:
            condiciones_cumplidas +=0


    print(f"Cumple {condiciones_cumplidas} condiciones")



verificacion_DUI(dui)
    