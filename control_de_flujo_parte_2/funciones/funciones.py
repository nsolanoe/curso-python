# crear una función que permita obtener:
# nombre
# fecha de nacimineto
# con los datos obtenidos calcular:
# edad actual de la persona
# imprimir un saludo que incluya que incluya su nombre y su edad actual

def edad():
    nombre = input("Ingresa aqui tu nombre: ")
    año_nacimiento = int(input("Ingresa aqui tu año de nacimiento: "))
    edad = 2023 - año_nacimiento
    print(f"{nombre} tiene {edad} años.")



