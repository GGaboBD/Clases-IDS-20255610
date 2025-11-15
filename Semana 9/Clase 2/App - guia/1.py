menu_activo = True

clientes = []
productos = []
pedidos = []


while menu_activo:  
    opcion = input("""
1: Mostrar productos
2: Agregar producto
3: Registrar nuevo cliente
4: Mostrar clientes
5: Registrar pedido
6: Mostrar pedidos del día
7: Mostrar categorías disponibles
8: Salir

Ingrese una opcion: """)


    if opcion == "1":
        if len(productos) == 0:
            print("Actualmente no hay productos")
        else:
            for producto in productos:
                print(f"Producto: {producto_nuevo}, Precio: {precio}, Codigo: {codigo}, Categoria: {categoria}")
    
    elif opcion == "2":
        codigo = input("Ingresa el codigo del producto: ")
        existe = False
        for p in productos:
            if p["codigo"] == codigo:
                existe = True
        if existe == True:
            print("El codigo ya existe")
        else:
            producto_nuevo = input("Ingresa el nombre del producto: ")
            categoria = input("Ingresa la categoria del producto: ")
            precio = float(input("Ingresa el precio del producto: $"))
            productos.append({"codigo": codigo, "productos": producto_nuevo, "categoria": categoria, "precio": precio})
        
    elif opcion == "3":
        codigo = input("Ingrese su codigo: ")
        existe = False
        for c in clientes:
            if c["codigo"] == codigo:
                existe = True
        if existe == True:
            print("El codigo ya existe")
        else:
            nombre = input("Ingrese su nombre: ")
            correo = input("Ingrese su correo: ")
            telefono = input("Ingrese su numero celular: ")
            clientes.append({"codigo": codigo, "nombre": nombre, "correo": correo, "telefono": telefono})
    
    elif opcion == "4":
        if len(clientes) == 0:
            print("Actualmente no hay clientes registrados")
        else:
            for cliente in clientes:
                print(f"codigo: {codigo}, nombre: {nombre}, correo: {correo}, telefono: {telefono}")

    elif opcion == "5":
        codigo_cliente = input("Ingrese su codigo de cliente: ")
        cliente_encontrado = False
        for c in clientes:
            if c["codigo"] == codigo_cliente:
                cliente_encontrado = True
        if cliente_encontrado == False:
            print("El codigo del cliente no ha sido registrado, registrelo primero XXX")
        else:
            if len(productos) == 0:
                print("No hay productos registrados en el menu")
            else:
                print("Productos disponibles:")
                for p in productos:
                    print(f"- {codigo}\t {producto}: ${precio}")

                lista_productos = []
                total = 0
                sub_menu = True
                codigo_producto_encontrado = False
                while sub_menu:
                    codigo_producto = input("Ingresa el codigo del producto que deseas agregar a tu pedido(Ingresa # para terminar pedido): ")
                    for cp in productos:
                        if cp["codigo"] == codigo_producto:
                            codigo_producto_encontrado = True
                    if codigo_producto_encontrado == False:
                        print("El codigo del producto no es valido")
                    else:
                        lista_productos.append(codigo_producto)
                        total = total + cp["precio"]
                        print(f"{cp["nombre"]}: ${cp["precio"]} - Agregado al pedido")

                if len(lista_productos) >0:
                    pedidos.append({"cliente": codigo_cliente, "productos": lista_productos, "total": total})
                    print(f"Su pedido ha sido enviado, su total es de ${total:.2f}")
                else:
                    print("El cliente no ha realizado ningun pedido :(")