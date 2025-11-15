semana = {}

semana["uno"] = "Lunes"
semana["dos"] = "Martes"
semana["tres"] = "Miercoles"
semana["cuatro"] = "Jueves"
semana["cinco"] = "Viernes"
semana["seis"] = "Sabado"
semana["siete"] = "Domingo"


semana_0 = {"uno": "OMG :0"}


print(semana)
print(semana_0)
print(semana["cuatro"])

print(semana.items()) #Te pone en lista los elementos del diccionario ('clave', 'valor')
print(semana.keys()) #Te pone en una lista las claves
print(semana.values()) #Te pone en una lista los valores


for v in semana.values():
    print(v)

print("#################")

for k, v in semana.items():
    print(f"dia {k}: {v}")

###Hacen un recorrido o construyen un orden como si fuera una lista

