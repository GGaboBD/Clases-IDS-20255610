def ordenar_pizza(tamaño, masa, *ingredientes):
    print(f"Usted a ordenado una pizza {tamaño} con masa de {masa} de:")
    for i in ingredientes:
        print(f"\t- {i}")


def registro_profesores(nombre, apellido, **materias):
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    
    for ciclo, materias in materias.items():
        print(f"\t - {ciclo}: \t {materias}")





def saludar_usuario(nombres):
    """Saludara usuario"""
    for nombre in nombres:
        print(f"Hola {nombre.capitalize()}")
