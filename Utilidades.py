# fuciones
def presentacion():
    # variables de entorno
    saludo = "Bienvenido al curso de Python"
    print(saludo)

    nombre = input("¿Cómo te llamas?")
    print("Encantado de concerte " + nombre)

    edad = input("¿Qué edad tienes?")

    if int(edad) >= 18:
        print("Ya puedes obtener el carnet de conducir")
    else:
        print("Aún no puedes conducir")