
my_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

#El orden esta invertido JHAJHASJHA, los ultimos conjuntos de codigo, son lo primero que vimos en clase, y el primero que esta aca arribita, es lo ultimo que vimos en clase

#Todos estos bloques de codigo con basados en el objeto de aqui arriba, que es my_string

"""
print(my_string.count("C")) #Cuenta cuantas veces aparece la letra C en la cadena #Salida: 1
print(my_string.count("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) 

#Al agregarle un punto luego del nombre de la varibale, veremos otras nuevas operaciones que podemos aplicarle a la variable

#Se podria decir que el punto es una funcion que se aplica al objeto, pero no se le llama funcion, sino que se le llama METODO
"""






"""
print("H" in my_string) #H esta en my_string? #Salida: True
print("HOLA" in my_string)
print("BCD" in my_string) #Salida: True

print("A" * 8) 

print(min(my_string))
print(max(my_string))
"""




"""
print(len(my_string)) #El len() cuenta todos los caracteres, iniciando DESDE 1, por eso, en la salida nos da 27 y no el 26 que buscabamos
print(my_string[0:27]) #La salida llega hasta el cuarto elemento, pero no al quinto (que es el indice 4) porque funciona como un limite x<4 pero no igual #Tambien se puede interpretar como: (cadena de valores que inicia desde 0: cadena de valores que inicia a contar desde 1) y por eso escribimos el cuarto valor embes del tercero que sale en la salida # si incluye al primer valor pero no al ultimo [0:4]
#Y aqui escribimos el rango de [0:27] porque empezo a contar desde 0 a diferencia del len() que empezo a contar desde 1

print(my_string[0:27:2]) #El tercer numero del rango, indica el salto que va a dar, en este caso de 2 en 2 #Salida: ACEGIKMOQSUWY #El primer valor del rango siempre se incluye
print(my_string[27:1:-1]) #Salida: ZYXWVUTSRQPONÑMLKJIHGFEDCBA #El -1 indica que va a ir en reversa, de atras para adelante #El primer valor del rango siempre se incluye
"""




"""
letra = int(input("Indique el indice de la letra a mostrar (del 0 al 4): ")) #El input siempre devuelve un string, por eso se usa int para convertirlo a entero
print(my_string[letra])"""


 

""""
print(my_string[2]) # Salida: C, dentro de los corchetes, se coloca el numero de su correspondiente caracter que quiero que salga, iniciando a contar desde 0 
print(len(my_string))  # Salida: 5 #string, cadena de caracteres"""





""" 
Itemingresar = input("Ingrese el item: ")
print (f"el item ingresado es: {Itemingresar}")

s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3)) # La funcion "len()" sirve para contar la cantidad de caracteres que hay en una variable.
"""