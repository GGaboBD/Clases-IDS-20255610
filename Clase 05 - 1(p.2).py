### Ejercicio de Tuplas

#Tupla es INMUTABLE, no se puede cambiar
#Una lista si es mutable

#Ambas son lo mismo, la diferencia es que la lista es mutable, y la tupla es inmutable, tambien que la lista usa[] y la tupla ()

tupla1 = (1,12,255,1289,60,000)
lista1 = [1,12,255,1289,60,000]
print(len(tupla1))
print(tupla1[4])
print(tupla1[2:6])

lista1[-1] = 3 #Se reemplaza el ultimo valor, con un 3

#lista1. #A las listas, los comandos con el punto, son distintos a los strings y tuplas


print(tupla1)

print(lista1)

