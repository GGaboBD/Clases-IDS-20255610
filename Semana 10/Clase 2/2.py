def registro_usuarios(nombre, appellido,inicial=""):
    """Construir un nombre a partir de sus componentes"""
    nombre_completo = f"{nombre} {inicial} {appellido}"
    return nombre_completo

print(registro_usuarios(input("Ingrese su nombre: "), input("Ingrese su apellido: "), input("Ingrese su inicial: ")))