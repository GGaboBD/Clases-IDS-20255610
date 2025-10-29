"""nombre = "Antonio"
repetidos = nombre.lower().count("a")
print(repetidos)"""

nombres = ["Maria","Ana", "Antonio", "Ana", "Jose"]


"""### Metodo brusco

repetidos_a = 0
repetidos_a = repetidos_a + nombres[0].lower().count("a") 
repetidos_a = repetidos_a + nombres[1].lower().count("a")
repetidos_a = repetidos_a + nombres[2].lower().count("a")
repetidos_a = repetidos_a + nombres[3].lower().count("a")

print(repetidos_a)
"""


print(nombres.index("Antonio"))

print(nombres.index("Ana",1))
print(nombres.index("Ana",nombres.index("Ana")+1))

