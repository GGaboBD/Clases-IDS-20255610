#Vamos a crear un diccionario!!

mi_gato = {
    "nombre": "pelusa", 
    "edad": 3, 
    "personalidad": "simpatico"}


mi_gato_2 = {
    1: "pelusa", 
    2: 3, 
    3: "simpatico"}


abys_cat = {
    "personalidad": "simpatico",
    "nombre": "pelusa",
    "edad": 3
}



print(mi_gato["nombre"])
print(type(mi_gato))
print(len(mi_gato))

copia = abys_cat == mi_gato

print(copia)