# Crear una script que indique si el usuario es mayor de edad
# Realizado por Nicolas Solano


edad = int(input("introducir aqui la edad:"))

if edad >= 18 and edad < 60:
   print("usted es mayor de edad")
elif edad < 18 and edad > 0:
   print("usted es menor de edad")

elif edad >= 65:
   print("usted es de la tercera edad")

else :
    print("ingrese un valor valido")