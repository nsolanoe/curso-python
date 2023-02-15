"""Calcular el área y el perímetro de un Rectángulo,
Crear las variables
alto (int)
ancho (int)
Área: alto * ancho
Perímetro: alto + ancho
"""
# Realizado por Nicolas Solano

alto = int(input("Ingrese la altura del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))


area = alto * ancho
perimetro = alto + alto + ancho +ancho

print("el area del rectagulo es:", area)
print("el perimetro del rectangulo es:", perimetro)
