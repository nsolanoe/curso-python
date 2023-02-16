# Dado un número de 5 dígitos, devolver el número en orden inverso.
# Realizado por Nicolas Solano




num1 = str(input("Ingrse el primer numero: "))
num2 = str(input("Ingrse el segundo numero: "))
num3 = str(input("Ingrse el tercer numero: "))
num4 = str(input("Ingrse el cuarto numero: "))
num5 = str(input("Ingrse el quinto numero: "))


numero = num1, num2, num3, num4, num5
num_invertido = numero[::-1]   

print(num_invertido)   