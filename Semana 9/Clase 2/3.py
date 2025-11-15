
menu_activo = True

### Requisito 1
codigos_clientes = {}
nombres_clientes = {}
correos_clientes = {}
numeros_telefonicos_clientes = {}

Registro = {}
cantidad_clientes = 0

codigos = []
nombres = []
correos = []
numeros_telefonicos = []

### Requisito 2
codigos_productos = {}
nombres_productos = {}
categorias_productos = {}
precios_productos = {}

Registro_productos = {}
cantidad_productos = 0

codigo_producto = []
nombre_producto = []
categoria_producto = []
precio_producto = []


################################################################################################################
while menu_activo:
    opcion = input("" \
    "1: Mostrar productos. " \
    "2: Agregar producto. " \
    "3: Registrar nuevo cliente. " \
    "4: Mostrar clientes. " \
    "5: Registrar pedido. " \
    "6: Mostrar pedidos del día. " \
    "7: Mostrar categorías disponibles " \
    "8: Salir. : ")
    
    if opcion == "2":
        cantidad_productos += 1
        codigo_producto = input("Ingresa el codigo del producto: ")
        nombre_producto = input("Ingresa el nombre del producto: ")
        categoria_producto = input("Ingresa la categoria del producto: ")
        precio_producto = input("Ingresa el precio del producto: ")

        codigos_productos[f"Codigo del producto {cantidad_productos}"] = codigo_producto
        nombres_productos[f"Nombre del producto {cantidad_productos}"] = nombre_producto
        categorias_productos[f"Categoria del producto {cantidad_productos}"] = categoria_producto
        precios_productos[f"Precio del producto {cantidad_productos}"] = precio_producto

        Registro_productos = codigos_productos, nombres_productos, categorias_productos, precios_productos
        

    elif opcion == "3":
        cantidad_clientes += 1
        codigos = input("Ingresa tu codigo: ")
        nombres = input("Ingresa tu nombre: ")
        correos = input("Ingresa tu correo: ")
        numeros_telefonicos = input("Ingresa tu numero telefonico: ")

        codigos_clientes[f"Codigo {cantidad_clientes}"] = codigos
        nombres_clientes[f"Nombre {cantidad_clientes}"] = nombres
        correos_clientes[f"Correo {cantidad_clientes}"] = correos
        numeros_telefonicos_clientes[f"Numero telefonico {cantidad_clientes}"] = numeros_telefonicos

        Registro = codigos_clientes, nombres_clientes, correos_clientes, numeros_telefonicos_clientes
    
    
    elif opcion == "5":
        codigo_del_ciente = input("Ingresa tu codigo: ")
        if codigo_del_ciente in codigos_clientes.values():
            if len(codigos_productos) > 0:
                print(f"{nombres_productos.values()} con el codigo {codigos_productos.values()}")
    
