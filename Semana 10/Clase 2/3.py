def registro_usuarios(nombre, appellido,inicial="", edad = 0):
    """Construir un nombre a partir de sus componentes"""
    if edad:
        nombre_completo = f"La persona {nombre} {inicial} {appellido} tiene {edad} años"
    else:
        nombre_completo = f"La persona es {nombre} {inicial} {appellido}"
    return nombre_completo

print(registro_usuarios(input("Ingrese su nombre: "), input("Ingrese su apellido: "), input("Ingrese su inicial: "), input("Ingrese su edad: ")))