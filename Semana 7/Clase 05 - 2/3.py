nombres = ["Ana", "Antonio", "Ana", "Jose", "Carlos", "Gabriel"]

print(nombres)
nombres.remove("Carlos")
print(nombres)

nombre_borrado = nombres.pop(3) #.pop te borra el dato pero a su vez te lo guarda
print(f"Nombre borrado: {nombre_borrado}")
print(nombres)

nombres.reverse() #Te invierte el orden de la lista
print(nombres)