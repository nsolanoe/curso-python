# Crear un script que encuentre el elemento menor de una lista
# Realizado por Nicolás Solano

def elemento_menor(lista):    
    menor = min(lista)
    
    return menor

elemento_1 = int(input("ingrese el primer elemento de su lista: "))
elemento_2 = int(input("ingrese el segundo elemento de su lista: "))
elemento_3 = int(input("ingrese el tercer elemento de su lista: "))
elemento_4 = int(input("ingrese el cuarto elemento de su lista: "))
elemento_5 = int(input("ingrese el quinto elemento de su lista: "))

lista = [elemento_1, elemento_2, elemento_3, elemento_4, elemento_5]
menor = elemento_menor(lista)
print("El elemento menor de la lista es:", menor)

