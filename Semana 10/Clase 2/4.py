def saludar_usuario(nombres):
    
    usuarios.append(input("Ingresa la persona a saludar: "))

    for nombre in nombres:
        print(f"Hola {nombre}")

    


usuarios = []



saludar_usuario(usuarios)