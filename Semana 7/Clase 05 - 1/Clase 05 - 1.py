lista = [1,2,"tres", ["lunes", "martes", "miercoles"]]
print(lista[3][2][3])

lista1 = ["lunes", "martes", "miercoles"]
semana = lista1 + ["jueves", "viernes", "sabado"]

print(semana)
print(len(semana))

semana[2] = "MIERCOLES"
print(semana)


semana.append(input("Escriba un siguiente dia: ")) #.append significa agregar el valor ingresado al final
print(semana)

semana.insert(4, input("Ingresa el dia viernes en mayusculas: ")) #Se agrega en la posicion 4
print(semana)