import random
import string

# Función para generar la contraseña
def generar_contrasena(longitud, incluir_numeros, incluir_simbolos):

    # Estructura de datos
    caracteres = list(string.ascii_letters)

    # Condicionales
    if incluir_numeros == "s":
        caracteres += list(string.digits)

    if incluir_simbolos == "s":
        caracteres += list(string.punctuation)

    contrasena = ""

    # Bucle
    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


# Programa principal
print("=== GENERADOR DE CONTRASEÑAS ===")

# Manejo de datos
longitud = int(input("¿Cuántos caracteres tendrá la contraseña? "))

# Condicional
if longitud <= 0:
    print("Error: la longitud debe ser mayor a 0")
else:
    incluir_numeros = input("¿Desea incluir números? (s/n): ").lower()
    incluir_simbolos = input("¿Desea incluir símbolos? (s/n): ").lower()

    # Llamada a la función
    contrasena = generar_contrasena(longitud, incluir_numeros, incluir_simbolos)

    print("\nContraseña generada:")
    print(contrasena)
