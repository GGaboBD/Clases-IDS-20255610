menu_activo = True

#Lista de diccionarios [{a: b}]
clientes = []
productos = []
pedidos = []

while menu_activo:
    opcion = input(""" 
------------------------------------
1: Mostrar productos
2: Agregar producto
3: Registrar nuevo cliente
4: Mostrar clientes
5: Registrar pedido
6: Mostrar pedidos del día
7: Mostrar categorías disponibles
8: Salir
-----------------------------------
                   
""") #Con triple comillas dobles podes separar lineas: """  """
    
    if opcion == "1":
        if len(productos) == 0:
            print("No hay productos registrados")
        else:
            for p in productos:
                print(f"Codigo: {p["codigo"]} Nombre: {p["nombre"]} Categoria: {p["categoria"]} Precio: ${p["precio"]}")

    elif opcion == "2": 
        codigo = input("Ingrese el codigo del producto: ")
        existe = False
        for p in productos:
            if p["codigo"] == codigo:
                existe = True
        if existe == True: 
            print("El codigo del producto ya existe XXX")
        else:
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoria del producto: ")
            precio = float(input("Ingrese el precio del producto: $"))
            productos.append({"codigo": codigo, "nombre": nombre, "categoria": categoria, "precio": precio})
    
    elif opcion == "3":
        codigo = input("Ingresa tu codigo: ")
        #Aqui se validara si es codigo unico
        existe = False
        for c in clientes:
            if c["codigo"] == codigo:
                existe = True
        if existe:
            print("El codigo ya existe XXX")
        else: 
            nombre = input("Ingrese su nombre: ")
            correo = input("Ingrese su correo: ")
            telefono = input("Ingrese su numero celular: ")
            clientes.append({"codigo": codigo, "nombre": nombre, "correo": correo, "telefono": telefono})

    elif opcion == "4":
        if len(clientes) == 0:
            print("No hay clientes registrados")
        else:
            for c in clientes:
                print(f"codigo: {c["codigo"]}, Nombre: {c["nombre"]}, Correo: {c["correo"]}, Telefono: {c["telefono"]}")

    elif opcion == "5":
        codigo_cliente = input("Ingrese el codigo del cliente: ")
        cliente_encontrado = False
        for c in clientes:
            if c["codigo"] == codigo_cliente:
                cliente_encontrado = True
        if cliente_encontrado == False: #el "not" del "if not" invierte el valor de la variable oooo --> if cliente_encontrado (Que seria True) == False (Hacelo Falso):
            print("El cliente no ha sido encontrado, registrelo primero XXX")
        else:
            if len(productos) == 0:
                print("No hay productos registrados :(")
            else:
                print("Productos disponibles:")
                for p in productos:
                    print(f"- {p["nombre"]}: ${p["precio"]} --- Codigo: {p["codigo"]}")
                
                lista_productos = []
                total = 0
                sub_menu = True
                while sub_menu:
                    codigo_producto = input("Ingrese el codigo del producto (O escriba 'fin' para terminar orden): ")
                    
                    if codigo_producto.lower() == "fin":
                        sub_menu = False
                    
                    else: 
                        encontrado = False
                        for producto in productos:
                            if producto["codigo"] == codigo_producto:
                                encontrado = True
                                lista_productos.append(codigo_producto)
                                total = total + producto["precio"]
                                print(f"{producto["nombre"]} agregado al pedido")

                if len(lista_productos) > 0:
                    pedidos.append({"cliente": codigo_cliente, "productos": lista_productos, "total": total})
                    print(f"Pedido registrado, su total es de: ${total:,.2f}")
                else:
                    print("No se agregaron productos al pedido")
                
    elif opcion == "6":
        if len(pedidos) == 0:
            print("Actualmente no hay pedidos registrados")
        else:
            cantidad = 1
            for p in pedidos:
                print(f"Pedido #{cantidad}")
                print(f"Cliente: {"cliente"}")
                print("Productos")
                for prod in p["productos"]:
                    print(f"- {prod}")
                print(f"Total: ${p["total"]:,.2f}")
                cantidad += 1

    elif opcion == "7":
        if len(productos) == 0:
            print("No hay categorias disponibles")
        else:
            categorias = []
            for p in productos:
                if p["categoria"] not in categorias:
                    categorias.append(p["categoria"])
            
            print("Categorias disponibles:")
            for cate in categorias:
                print(f"- {cate}")


    elif opcion == "8":
        menu_activo = False
    
    else:
        print("Escoja una opcion de la lista por favor")