import random

# Función para generar la contraseña
def generar_contrasena(longitud, mayusculas, minusculas, numeros, simbolos):

    # Estructuras de datos
    letras_mayusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    letras_minusculas = list("abcdefghijklmnopqrstuvwxyz")
    lista_numeros = list("0123456789")
    lista_simbolos = list("!@#$%&*?")

    caracteres = []

    # Condicionales
    if mayusculas == "s":
        caracteres = caracteres + letras_mayusculas

    if minusculas == "s":
        caracteres = caracteres + letras_minusculas

    if numeros == "s":
        caracteres = caracteres + lista_numeros

    if simbolos == "s":
        caracteres = caracteres + lista_simbolos

    # Validación
    if len(caracteres) == 0:
        return "Debe seleccionar al menos un tipo de carácter."

    contrasena = ""

    # Bucle
    for i in range(longitud):
        contrasena = contrasena + random.choice(caracteres)

    return contrasena


# Programa principal
print("===================================")
print("   GENERADOR DE CONTRASEÑAS")
print("===================================")

# Manejo de datos
longitud = int(input("Ingrese la longitud de la contraseña: "))

# Condicional
if longitud <= 0:
    print("La longitud debe ser mayor que cero.")
else:
    mayusculas = input("¿Incluir letras mayúsculas? (s/n): ")
    minusculas = input("¿Incluir letras minúsculas? (s/n): ")
    numeros = input("¿Incluir números? (s/n): ")
    simbolos = input("¿Incluir símbolos? (s/n): ")

    # Llamada a la función
    resultado = generar_contrasena(longitud, mayusculas, minusculas, numeros, simbolos)

    print("\nContraseña generada:")
    print(resultado)
