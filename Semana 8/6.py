#limite 45 horas
valores = [[1,3,6],[2,7,4], [6,5,9], [1,10,20]]

horas = 0

for v in valores:
    for i in v:
        while horas <= 45:
            horas += i 

print(horas)
