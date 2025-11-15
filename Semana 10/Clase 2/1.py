def describir_mascota(nombre_animal: str, tipo_animal: str = "perro"):
    """Esta funcion describe una mascota"""
    print(f"Tengo un {tipo_animal.lower()}, y su nombre es {nombre_animal.capitalize()}")

describir_mascota(nombre_animal="Bruno")