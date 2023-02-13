# Ingresar nombre y apellido e imprimirlo al revés
# Realizado por Nicolás Solano

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")

nombre_reves = nombre[::-1]
apellido_reves = apellido[::-1]

print("Su nombre y apellido al revés es:", nombre_reves, apellido_reves)

