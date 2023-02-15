"""
Solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que
sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es: numeroMayor
"""
# Realizado por Nicolas Solano

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2 :
    print("el numero mayor es:", num1)
elif num1 == num2 :
    print("los dos numeros son iguales", num1, "=", num2)

else:
    print("el numero mayor es:", num2)        