# Crear un script que reciba una cantidad infinita de números hasta decir basta, luego que imprima la suma de los números ingresados.
# Realizado por Nicolas Solano

suma = 0
while True:
    numero = input("Ingresa un número (o escribe 'basta' para terminar): ")
    if numero.lower() == "basta":
        break
    suma += int(numero)

print("La suma de los números ingresados es:", suma)
