# Crear un script que indique cuantas vocales tiene una palabra
# Realizado por Nicolás Solano

palabra = input("Ingrese una palabra: ")

palabra = palabra.lower()

contador_vocales = 0

for letra in palabra:
    if letra in "aeiou":
        contador_vocales += 1

print("La palabra", palabra, "tiene", contador_vocales, "vocales.")