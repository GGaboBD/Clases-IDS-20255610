#Ahora veremos los args

def ordenar_pizza(tamaño, *ingredientes):
    print(f"Usted a ordenado una pizza {tamaño} de:")
    for i in ingredientes:
        print(f"\t- {i}")

ordenar_pizza(input("Ingrese el tamaño de la pizza: ").lower(), input("Ingrese el ingrediente: ").capitalize(), input("Ingrese el ingrediente: ").capitalize())