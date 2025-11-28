# Sera lo mismo pero el profe hara algo mas


while True: # Creamos un bucle para seguir con el menu
    try: # try = Intenta esto
        monto = len(int(input("Digite: ")))
        
        
        #monto = float(input("Monto a calcular: ")) #Mi error (excepcion) esta aqui
        """impuesto = round(monto + 25) # Si no da error, continua con el desarrollo
        print(f"el impuesto es de ${impuesto:,.2f}")"""



    except TypeError as te: # Si el error es de tipo "Tipo error"
        print(f"Se genera un error: ", te) # Y muestra "te"

    except ValueError as ve: # Si es un error de tipo "Error de valor" has esto:
        print("Es un error de valor:", ve)



    else: # Es opcional, se puede hacer igualmente en "try"
        impuesto = round(monto + 25) # Si no da error, continua con el desarrollo
        print(f"el impuesto es de ${impuesto:,.2f}")
        break # Termina el bucle de "while True"

    # Exista error o no, finally devuelve siempre lo que le indiquemos
    
    finally: # Despues de haber tratado la excepcion, deshagamos todo y volvamos a comenzar con la ejecucion de la funcion
        print("Hemos terminado la ejecucion de esta pregunta :D")
