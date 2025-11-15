birthday = {
    "Alice": "Abril 1",
    "Bob": "Diciembre 12",
    "Carol": "Marzo 4",
    "Carol": "Junio 18"
}


birthday["Gabo"] = "Julio 17"
#AQUI NO FUNCIONA .append()

for persona, fecha in birthday.items():
    print(f"El cumpleaños de {persona} es en {fecha}")


print(birthday["Gabo"])
print(birthday)

del birthday["Bob"] #del    te borra elementos del diccionario

print(birthday)


