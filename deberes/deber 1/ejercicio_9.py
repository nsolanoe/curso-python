""""
El objetivo del ejercicio es crear un sistema de calificaciones, tomando en cuenta la
siguiente información:
1. El usuario proporcionará un valor entre 0 y 10.
2. Si está entre 9 y 10: imprimir una A
3. Si está entre 8 y menor a 9: imprimir una B
4. Si está entre 7 y menor a 8: imprimir una C
5. Si está entre 6 y menor a 7: imprimir una D
6. Si está entre 0 y menor a 6: imprimir una F
7. Cualquier otro valor debe imprimir: Valor desconocido
Por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""
# Realizado por Nicolas Solano


calificacion = float(input("Ingrese su calificación: "))

if calificacion >= 9 and calificacion <= 10:
    print("felicitaciones tienes una A")
elif calificacion >= 8 and calificacion < 9:
    print("muy bien tienes una B")
elif calificacion >= 7 and calificacion < 8:
    print("tienes una C")
elif calificacion >= 6 and calificacion < 7:
    print("puedes mejorar tienes una D")
elif calificacion  >= 0 and calificacion <6:
    print("reprobaste tienes una F")
else:
    print("valor no permitido")

 
