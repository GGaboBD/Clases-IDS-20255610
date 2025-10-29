cantidad_alumnos = 25
nombre_profe = "Alvin"
nuevas_inscripciones = 0
nombre_profe = input("Ingrese el nombre del profesor: ") #input es el inverso de print, es decir, en vez de mostrar algo en pantalla, lo que hace es pedir un dato al usuario
nuevas_inscripciones = int(input("Nuevos alumnos: "))
print(type(nombre_profe))
print(nombre_profe)
print(cantidad_alumnos + nuevas_inscripciones) #El valor de "nuevas_inscripciones" es un valor que lo recibe como str (Texto) y no lo puedo modificar yo, por lo que ahora, a la linea 5 que es donde esta, le pondremos int (entero) antes del input
###INPUT FUNCIONA SIEMPRE COMO STR (TEXTO)###

