
usuario = "Alvin"
Cantidad_alumnos = 79
media_edad = 18.23882783278
monto_rifa_hope = 1232234.567896378627868721
inversion_evento = 98765.215486732

print(type(Cantidad_alumnos)) #type = tipo, la funcion type nos dice que tipo de dato es la variable que le pasamos entre los parentesis
print(type(media_edad))

print(type(Cantidad_alumnos) is int) #int = entero, esta formula con "is int" la usamos como decir "Es un entero???"
print(type(media_edad) is int) 

print("el usuario es", "Alvin", "y tiene", Cantidad_alumnos, "alumnos a su cargo") #Si en el nombre ponemos otro distinto al del dato/variable que definimos al inicio, dara error
print(" y la edad promedio es de", media_edad)

# f-string: viene de un texto, pero de un texto formateado, agregar una f es la sintaxis de creación de un f-string, que significa? las oraciones o palabras que van entre comillas, antesedidas por una f, tienen la capacidad de aceptar formatos y tomar variables dentro de este texto
print(f"El usuario es {usuario}", )
print(f"y en su aula con {Cantidad_alumnos - 4} pajaritos")
print(f" con edad promedio de {media_edad:.2f} años") #el :.2f es para limitar los decimales a 2 decimales LUEGO DEL PUNTO
print(f"colectaron {monto_rifa_hope:,.2f} como un donativo") #Al agregar la coma dentro de los :,.2f es para que los miles se separen con coma
print(f"y la totalidad de gastos fue de ${abs(inversion_evento):,.2f} dolares") #la funcion Abs, devuelve el valor absoluto de un número, es decir, su valor sin el signo. # El signo de dolar $ no afecta en nada

print(type(usuario)is str) #str = string, cadena de texto

Esta_lloviendo = False
print(type(Esta_lloviendo)is bool) #bool = booleano, verdadero o falso
print(type(monto_rifa_hope) is not bool)


""" 
nombre = "Alvin"
Apellido = "Portillo"
nombre_completo = nombre + " " + Apellido # + " " + significa un espacio entre las dos variables
print(nombre_completo)

#no podemos usar numeros en cadenas de texto, porque sino te arrojara error, un principio fundamental de la programación es que hay una clasificación de datos especificos para cada uno, y si mezclamos datos, dara error

# Porque son importantes los tipos de datos? Porque cuando trabajamos con tipos de datos, como los textos, lo que obtenemos es que en pantalla me muestre una solucion
"""





