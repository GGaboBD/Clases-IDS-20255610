"""def calcular_impuesto():
    pass # No hagas nada, continua con lo demas""" 




while True: # Creamos un bucle para seguir con el menu
    try: # try = Intenta esto
        monto = float(input("Monto a calcular: ")) #Mi error (excepcion) esta aqui
        """impuesto = round(monto + 25) # Si no da error, continua con el desarrollo
        print(f"el impuesto es de ${impuesto:,.2f}")"""

    except: # except = Si la linea 5 o "try" produce un error de excepcion has esto:
        print("Ese tipo de valores no es valido")

    else: # Es opcional, se puede hacer igualmente en "try"
        impuesto = round(monto + 25) # Si no da error, continua con el desarrollo
        print(f"el impuesto es de ${impuesto:,.2f}")
        break # Termina el bucle de "while True"

    # Exista error o no, finally devuelve siempre lo que le indiquemos
    
    finally: # Despues de haber tratado la excepcion, deshagamos todo y volvamos a comenzar con la ejecucion de la funcion
        print("Hemos terminado la ejecucion de esta pregunta :D")
