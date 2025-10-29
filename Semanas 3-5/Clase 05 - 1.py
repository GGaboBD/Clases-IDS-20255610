
nombre = "Alvin" #Corresponde a un tipo de dato #La estuctura es una cadena de caracteres!!!
palabra = "RECONOCER"
otra_palabra = "palabra"

print(len(nombre))

print(nombre [2])
print(nombre [0:5])

print(nombre[0:]) # Al no poner un numero de finalizacion, lo que le decimos a la maquina es que vaya desde el numero que inicia el rango, hasta el final.

print(len(palabra))
print(palabra[0::2])
print(palabra[::2])
print(palabra[::])
print(palabra[::-1])

print(otra_palabra[::-1])
#print(nombre[5:-6:-1])
#Palindro


############################

palabra2 = "sorbete"
print(palabra2[::-1])
print(palabra2==palabra2[::-1]) #Se compara si la palabra, escrita al revez, es igual a la palabra escrita de derecha a izquierda

numero = "255"
print(numero)
print(len(numero)) #En python, los numeros no tienen un largo

############################

mi_palabra = "jocote y avena"
print(mi_palabra)
mi_palabra_mayuscula = mi_palabra.upper() #upper es el objeto original, pero en su version en mayuscula
mi_palabra_cap = mi_palabra.capitalize() #capitalize sirve para hacer la primera letra de la oración, mayuscula
#Origen.dependiente()

print(mi_palabra_mayuscula)
print(mi_palabra_cap)

#index y count son metodos