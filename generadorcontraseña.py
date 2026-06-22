import random
import string

print("=== GENERADOR DE CONTRASEÑAS ===")

#Entrada del usuario
longitud = int(input("¿Cuántos caracteres tendrá la contraseña? "))

# ✔ ESTRUCTURA LÓGICA (condicionales)
if longitud <= 0:
    print("Error: la longitud debe ser mayor a 0")
else:
    usar_numeros = input("¿Desea incluir números? (s/n): ")
    usar_simbolos = input("¿Desea incluir símbolos? (s/n): ")

    # Base de caracteres
    caracteres = string

    # ✔ ESTRUCTURA LÓGICA (condicionales)
    if usar_numeros == "s":
        caracteres += string

    if usar_simbolos == "s":
        caracteres += string

    contrasena = ""

    # ✔ ESTRUCTURA REPETITIVA (bucle)
    for i in range(longitud):
        contrasena +=(caracteres)

    # Resultado final
    print("\nContraseña generada:")
    print(contrasena)