#args se usa para crear listas y se usa *

#kwargs se usa para crear diccionarios y se usan **

def registro_profesores(nombre, apellido, **materias):
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    
    for ciclo, materias in materias.items():
        print(f"\t - {ciclo}: \t {materias}")


registro_profesores(
    "Alvin",
    "Portillo",
    ciclo1 = ["BD1", "IIJ", "A&GD"],
    Ciclo2 = ["DAI", "BD2", "SINE"],
    Ciclo3 = ["IDS", "FPEN", "PAD"]
)