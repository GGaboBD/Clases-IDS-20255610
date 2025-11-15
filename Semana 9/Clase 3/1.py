#Nombre de la funcion(Argumentos) --> print("Hola") 
# Argumentos: 
# - Ninguno
# - Uno
# - Muchos


#def --> Definir una funcion #Definir el nombre con el que llamare a la funcion



#Cada archivo de python se llama "modulo"




#ESTE ES UN DOCSTRING DE MODULO
# VAMOS A CREAR VARIAS FUNCIONES


def saludar(): #Las variables creadas dentro de la funcion, son exclusivas de la funcion
    """Es una funcion que va a saludar"""
    nombre = input("Digite su primer nombre: ")
    apellido = input("Digite su primer apellido: ")
    nombre_completo = f"{nombre.title()} {apellido.title()}" #.title() hace que la primera letra sea mayuscula
    print(f"Hola {nombre_completo}")


def saludar_con_parametro(nombre, apellido): #(nombre) esta asi como con un color mas oscuro porque es un parametro que no a sido utilizado en la funcion
    """Es una funcion para saludar con parametros"""
    
    print(f"Hola {nombre.title()} {apellido.title()}")

#Ahora, para poder trabajar, necesita un parametro!!!! #(nombre) es el parametro y ("Fer") es el argumento

def describir_mascota(animal, nombre_mascota):
    """Vamos a describir mascotas"""
    print(f"Tengo un {animal.lower()} y su nombre es {nombre_mascota.title()}")

describir_mascota(nombre_mascota = "firulais", animal = "perro")
describir_mascota(
    input("Escribe que animal es tu mascota: "), 
    input("Ingresa el nombre de tu mascota: ")
    )

