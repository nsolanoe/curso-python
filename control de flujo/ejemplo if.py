#programa para determinar si una persona es menor de edad, mayor de de edad o adulto mayo

edad = int(input("introducir aqui la edad:"))

if edad >= 18 and edad < 60:
   print("usted es mayor de edad")
elif edad < 18 and edad > 0:
   print("usted es menor de edad")

elif edad >= 60:
   print("usted es de la tercera edad")

else :
    print("ingrese un valor valido")